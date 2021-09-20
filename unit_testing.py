import unittest
from unittest import mock
import requests
import web_scrapper
from unittest.mock import patch

class Test_Web_Scraping(unittest.TestCase):
    def test_0_top_movie(self):
        self.assertRaises(TypeError,web_scrapper.top_movie("https://www.imdb.com/chart/top/","asds"))
        self.assertEqual(web_scrapper.top_movie("https://",5),None)
        print("top_moive function tested successful")
    
    def test_1_get_synopsis(self):
        self.assertRaises(TypeError,web_scrapper.get_synopsis("mknj"))
        print("get_synopsis function tested succesful")
        
    def test_3_bag_of_words(self):
        pass
        
            

if __name__ == '__main__':
    unittest.main()
