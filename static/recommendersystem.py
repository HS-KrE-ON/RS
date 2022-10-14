'''Module to match mapper to IDs'''
import pickle as pkl
import pandas as pd

# pylint: disable=consider-using-with
open_file = open('data/movie_mapper.pkl', "rb")
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

    df_neighbours = pd.read_csv('data/neighbours_increase.csv')
    df_distances = pd.read_csv('data/distances.csv')

    neighbours = df_neighbours.iloc[idx-1]
    neighbours = list(neighbours.tolist())[:0:-1]

    distances = df_distances.iloc[idx-1]
    distances = list(distances.tolist())[:0:-1]

    raw_recommends = list(zip(neighbours, distances))

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
        idx = convert_movie(convert= movie_to_idx, fav_movie=my_favorite)
        make_recommendation(idx)

    sort_combinations(combination)
    combination.clear()
    return frontend_input
    #print_recommendations(combination)
# pylint: disable=inconsistent-return-statements

def convert_movie(convert, fav_movie):
    '''
    convert movie strings to id
    '''
    # pylint: disable=unnecessary-comprehension
    mapper=convert
    idx = []
    entry = fav_movie[0]
    vorwaerts_mapper = {k: v for k, v in mapper.items()}
    idx=vorwaerts_mapper[entry]
    return idx

#Entry for recommendations
def recommendate(array):
    """
    return sorted movie neighbours
    """
    frontend_input.clear()
    process_recommendations(array)
    array=[]
    return frontend_input
