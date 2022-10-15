'''Unit Test for Recommendations'''
import unittest
from static.recommendersystem import recommendate
from static.script.js import submitMovies

class TestRecommendation(unittest.TestCase):
    '''
    Test the recommendations
    '''
    def test_output_correct(self):
        '''Test if output list is equal to expected list'''
        expected_list=['When Dinosaurs Roamed America (2000)',
                       'Chased by Dinosaurs: Three Walking with Dinosaurs Adventures (2003)',
                       'Walking with Prehistoric Beasts (2001)',
                       'Allosaurus: A Walking with Dinosaurs Special (2001)',
                       'Walking with Cavemen (2003)',
                       'Walking with Dinosaurs (1999)',
                       'Prehistoric America: A Journey Through the Ice Age and Beyond (2003)',
                       'National Geographic: Dinosaur Hunters: Secrets of the Gobi Desert (2002)',
                       'Prehistoric Planet: The Complete Dino Dynasty (2002)',
                       'Before We Ruled the Earth: Hunt or Be Hunted (2003)']
        output_list = recommendate(['Dinosaur Planet (2003)'])
        self.assertEqual(expected_list, output_list)

    def test_output_empty(self):
        '''Test if the output array is empty'''
        empty_list=[]
        output_list = recommendate(['Dinosaur Planet (2003)'])
        self.assertNotEqual(output_list, empty_list)

    def test_frontend(self):
        '''Test if frontend is reachable'''
        empty_list=[]
        movies =['Dinosaur Planet (2003)']
        output_list = submitMovies(movies)
        self.assertNotEqual(output_list, empty_list)

if __name__ == '__main__':
    unittest.main()
