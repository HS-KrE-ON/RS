'''Module to match mapper to IDs'''
import pickle as pkl
import pandas as pd
from fuzzywuzzy import fuzz

# pylint: disable=consider-using-with
open_file = open('/data/movie_mapper.pkl', "rb")
movie_to_idx = pkl.load(open_file)
open_file.close()

combination = []
frontend_input=[]

def make_recommendation (fav_movie):
    """
    Get predictions from static knn model
    """
    neighbours = []
    distances = []

    idx = fav_movie

    df_neighbours = pd.read_csv('/data/neighbours_increase.csv')
    df_distances = pd.read_csv('/data/distances.csv')

    neighbours = df_neighbours.iloc[idx]
    neighbours = list(neighbours.tolist())

    distances = df_distances.iloc[idx]
    distances = list(distances.tolist())

    raw_recommends = list(zip(neighbours, distances))[:0:-1]

    combine_recommendation(raw_recommends)
    return neighbours

def combine_recommendation(raw_recommends):
    '''
    Combines all recommendations per movie into one array, so that the data can be sorted afterwards
    '''
    for _, (idx, dist) in enumerate(raw_recommends):
        combination.append((idx,dist))
    return combination

def sort_combinations(list_combinations):
    '''
    Takes the list of of all recommendations and sort the results by the distance
    '''
    # pylint: disable=unused-argument
    list_combinations.sort(key=lambda tup:tup[1], reverse=False)
    list_combinations = list_combinations[:10]
    print_recommendations(list_combinations)
    return frontend_input

def print_recommendations(list_recommendations):
    '''
    Print output of the input of the recommendations
    '''
    # pylint: disable=consider-using-f-string
    mapper=movie_to_idx
    reverse_mapper = {v: k for k, v in mapper.items()}
    #print(list)
    print("\nAufgrund der Filmkombination können folgende Filme vorgeschlagen werden:\n")
    for i, (idx, dist) in enumerate(list_recommendations):
        dist= (1-dist)*100
        print('{0}: {1}, with accordance of {2}'.format(i+1,
                                                        reverse_mapper[idx],
                                                        round(dist,2))+'%')
        #input for frontend:
        frontend_input.append(reverse_mapper[idx])
        #frontend_input.append((reverse_mapper[idx],str(round(dist,2))+'%'))
    return frontend_input

def process_recommendations(list_of_entries):
    '''
    Processing the input array - first method which calls the recommendations
    '''
    for ele in list_of_entries:
        my_favorite = [ele]
        idx = fuzzy_matching(movie_to_idx, fav_movie=my_favorite, verbose=True)
        make_recommendation(idx)

    sort_combinations(combination)
    return frontend_input
    #print_recommendations(combination)
# pylint: disable=inconsistent-return-statements

def fuzzy_matching(mapper, fav_movie, verbose=True):
    """
    return the closest match via fuzzy ratio. If no match found, return None
    """
    # pylint: disable=unused-argument
    # pylint: disable=inconsistent-return-statements
    match_tuple = []
    # get match
    for title, idx in mapper.items():
        ratio = fuzz.ratio(title.lower(), fav_movie)
        if ratio >= 60:
            match_tuple.append((title, idx, ratio))
     # sort
    match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
    if not match_tuple:
        print('Oops! No match is found')
        return
    #if verbose:
    #print('Vorschläge auf Grundlage der FuzzyTechniques:
    #{0}\n'.format([x[0] for x in match_tuple]))
    return match_tuple[0][1]

#Entry for recommendations
def recommendate(array):
    """
    return sorted movie neighbours
    """
    frontend_input.clear()
    process_recommendations(array)
    array=[]
    return frontend_input
