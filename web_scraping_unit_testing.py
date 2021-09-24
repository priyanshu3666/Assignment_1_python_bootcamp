import unittest
import logging
import web_scrapper
from unittest import mock
from unittest.mock import patch



class Test_Web_Scraping(unittest.TestCase):
    def test_1_top_movie(self):
        self.assertRaises(TypeError,web_scrapper.top_movie("https://www.imdb.com/chart/top/","asds"))
        self.assertEqual(web_scrapper.top_movie("https://",5),None)
        logging.info("\ntop_moive function tested successful")
    
    def test_2_get_synopsis(self):
        self.assertRaises(TypeError,web_scrapper.get_synopsis("mknj"))
        logging.info("\nget_synopsis function tested succesful")
        
    def test_3_bag_of_words(self):
        self.assertEqual(web_scrapper.bag_of_words('ram is shyam'),['ram shyam'])
        logging.info("\nbag_of_words() function tested successful")
        
    def test_4_fetchting_movie_data(self):
        self.assertRaises(TypeError,web_scrapper.fetchting_movie_data(4515))
        logging.info("\nfetching_movie_data() function tested successfully")
        
    def test_5_search_movies_data(self):
        with mock.patch('builtins.input', return_value = "Crime"):
            assert web_scrapper.search_movies_data() == ['The Godfather', 'The Godfather: Part II', 'The Dark Knight', '12 Angry Men']
            logging.info("\n search_movies_data() function successfully tested")
if __name__ == '__main__':
    unittest.main()
