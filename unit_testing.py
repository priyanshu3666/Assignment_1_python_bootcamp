import unittest
from unittest import mock
import requests
import web_scrapper
from unittest.mock import patch

class Test_Web_Scraping(unittest.TestCase):
    def test_top_movie(self):
        self.assertRaises(TypeError,web_scrapper.top_movie("https://www.imdb.com/chart/top/","asds"))
        self.assertEqual(web_scrapper.top_movie("https://",5),None)
    
    def test_get_synopsis(self):
        pass
        

if __name__ == '__main__':
    unittest.main()