import unittest
import logging
import web_scrapper



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
        self.assertEqual(web_scrapper.search_movies_data(),[{'title': 'tt0068646', 'Synopsis': "['During early shot scene Vito Corleone returns home people carry stairs Marlon Brando put weights body bed prank make harder lift']", 'Genre': 'Crime, Drama', 'Actors': 'Marlon Brando, Al Pacino, James Caan'}, {'title': 'tt0071562', 'Synopsis': "['Robert De Niro spent four months learning speak Sicilian language order play Vito Corleone Nearly dialogue character speaks film Sicilian']", 'Genre': 'Crime, Drama', 'Actors': 'Al Pacino, Robert De Niro, Robert Duvall'}, {'title': 'tt0050083', 'Synopsis': "['At beginning film cameras positioned eye level mounted wideangle lenses give appearance greater distance subjects As film progresses cameras slip eye level By end film nearly shot eye level closeup telephoto lenses increase encroaching sense claustrophobia']", 'Genre': 'Crime, Drama', 'Actors': 'Henry Fonda, Lee J. Cobb, Martin Balsam'}])
        logging.info(" search_movies_data() function tested successfully")
if __name__ == '__main__':
    unittest.main()
