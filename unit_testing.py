import unittest
from unittest import mock
import requests
import web_scrapper
from unittest.mock import patch

class Test_Web_Scraping(unittest.TestCase):
    def test_1_top_movie(self):
        self.assertRaises(TypeError,web_scrapper.top_movie("https://www.imdb.com/chart/top/","asds"))
        self.assertEqual(web_scrapper.top_movie("https://",5),None)
        print("\ntop_moive function tested successful")
    
    def test_2_get_synopsis(self):
        self.assertRaises(TypeError,web_scrapper.get_synopsis("mknj"))
        print("\nget_synopsis function tested succesful")
        
    def test_3_bag_of_words(self):
        self.assertEqual(web_scrapper.bag_of_words('ram is shyam'),['ram shyam'])
        print("\nbag_of_words() function tested successful")
        
    def test_4_fetchting_movie_data(self):
        self.assertRaises(TypeError,web_scrapper.fetchting_movie_data(4515))
        
    
        
            

if __name__ == '__main__':
    unittest.main()
