from urllib.request import BaseHandler
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests,bs4,re,csv,os,logging
from string import punctuation

#creating logger file 
logging.basicConfig(filename="web_scrapper_logger.log",format='%(asctime)s %(message)s',filemode='w')
logger_obj=logging.getLogger()
logger_obj.setLevel(logging.DEBUG)
movie_id_list =[]
synopsis_list = []
movie_data_dict = {}
Omdb_key = "64a6542a"               # apikey for OBDb website
fields = ['title','Movie_Name','Synopsis','Genre','Actors']

#top_movie function  return the list of top n movies from IMDB website
def top_movie(url,top_num):
    try:
        request_ = requests.get(url)
        soup =bs4.BeautifulSoup(request_.text,'lxml')
        for num in range(top_num):
            class_content  = soup.select('.titleColumn')[num]('a')[0]['href']
            movie_id_list.append((str(class_content).split("/"))[2])
        return movie_id_list
    except TypeError:
        logging.error("top num should be  int ")
    except requests.exceptions.InvalidURL:
        logging.error("invalid url")
    except requests.exceptions.ConnectionError:
        logging.error("Internet connection problem,please check your connection  ")    
    except requests.exceptions.MissingSchema :
        logging.error("provide  url ")

#get_synopsis return the list of synopsis of movie_id from movies_id_list
def get_synopsis(movies_id):
    try:
        base_url = "https://www.imdb.com/title/"
        for movie_id in movies_id:
            request_ = requests.get(base_url+movie_id)
            if request_.status_code ==200:
                soup = bs4.BeautifulSoup(request_.text,'lxml')
                synopsis_list.append(soup.select('.ipc-html-content.ipc-html-content--base')[1].getText())
            else:
                logging.error("Invalid url")
        return synopsis_list
    except TypeError :
        logging.error("none type returned")

#this function return a list od bag_of_words
def bag_of_words(string_):       
        try:
            new_str = string_.translate(str.maketrans("", "", punctuation))
            all_stopwords = stopwords.words('english')
            text_tokens= [word for word in word_tokenize(new_str) if word.isalnum()] 
            bag_of_words = [word for word in text_tokens if not word in all_stopwords]
            filtered_string = [' '.join(bag_of_words)]
            return filtered_string
        except TypeError:
            logging.error("passed empty  argument")
    

# creating a api that return movie data
def fetchting_movie_data(movies_id_list):
    try:
        for movie_id  in movies_id_list:
            pattern = r"\D{2}\d{7}"
        
            if re.compile(pattern).match(movie_id).group()==movie_id:
                fetched_data = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={Omdb_key}")
                synopsis_data = fetched_data.json()
        
            try :
                temp_dict = {}
                temp_dict['Synopsis'] = movie_data_dict[f'{movie_id}']
                temp_dict['Genre'] = synopsis_data['Genre']
                temp_dict['Actors'] = synopsis_data['Actors']
                temp_dict['Movie_Name'] = synopsis_data['Title']
                movie_data_dict[f'{movie_id}'] =temp_dict
            except KeyError:
                logging.error("key not found")
    except TypeError:
            logging.error("movie_id is not int ")
    return movie_data_dict

def dict_to_csv_writer():
    file_name = 'movies_dict_csv.csv'
    
    if os.path.exists(file_name):
        file_ = open(file_name,'r')
        file_reader = csv.DictReader(file_)
        for row in file_reader:
            for item in movie_id_list:
                try:
                    if row['title'] == item:
                        movie_data_dict.pop(item)
                    else:
                        return KeyError
                except KeyError:
                    logging.error("key not found")
        file_.close()
        if len(movie_data_dict) > 0:
            with open(file_name,'a') as file:
                csv_writer_ = csv.DictWriter(file,fields)
                for key in movie_data_dict:
                    csv_writer_.writerow({field: movie_data_dict[key].get(field) or key for field in fields})
    else:
        with open(file_name,'w') as csv_file:
            csv_writer_ = csv.DictWriter(csv_file,fields)
            csv_writer_.writeheader()
            for key in movie_data_dict:
                csv_writer_.writerow({field: movie_data_dict[key].get(field) or key for field in fields})

def search_movies_data():
    
    user_input = input("Enter Genre or Actors ,keep in mind it is case sensitve!! ")
    if user_input and not user_input.isdigit():
        with open('movies_dict_csv.csv', 'r') as file_:
            csv_reader = csv.DictReader(file_)
            filtered_data = [row for row in csv_reader if user_input in row['Actors'] or user_input in row['Genre']]
            filter_movies_name = []
            for index in range(len(filtered_data)):
                filter_movies_name.append(filtered_data[index]['Movie_Name'])
            print(filter_movies_name)
            return filter_movies_name

if __name__ == '__main__':
    logging.info(top_movie("https://www.imdb.com/chart/top/",5))
    logging.info(get_synopsis(movie_id_list))
    num =0
    for movie_id in movie_id_list:
        movie_data_dict[movie_id] = bag_of_words(synopsis_list[num])
        num+=1
    logging.info(movie_data_dict)
    logging.info(fetchting_movie_data(movie_id_list))
    dict_to_csv_writer()
    logging.info(movie_data_dict)
    logging.info(search_movies_data())
    
    
