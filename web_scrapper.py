from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
import bs4
import re
from string import punctuation
import csv
import os



#top_movie function  return the list of top n movies from IMDB website
def top_movie(url,top_num):
    try:
        request_ = requests.get(url)
        soup =bs4.BeautifulSoup(request_.text,'lxml')
        movie_id_list =[]
        for num in range(top_num):
            class_content  = soup.select('.titleColumn')[num]('a')[0]['href']
            movie_id_list.append((str(class_content).split("/"))[2])
        return movie_id_list
    except TypeError:
        print("top_num should be an integer")
    except requests.exceptions.InvalidURL:
        print("invalid url")
    except requests.exceptions.MissingSchema :
        print("provide  url ")


#get_synopsis return the list of synopsis of movie_id from movies_id_list
def get_synopsis(movies_id):
    try:
        base_url = "https://www.imdb.com/title/"
        synopsis_list = []
        for movie_id in movies_id:
            request_ = requests.get(base_url+movie_id)
            soup = bs4.BeautifulSoup(request_.text,'lxml')
            synopsis = soup.select('.ipc-html-content.ipc-html-content--base')[1]
            synopsis_list.append(synopsis.getText())
        return synopsis_list
    except TypeError :
        print("none type returned")

movie_id_list = top_movie("https://www.imdb.com/chart/top/",5)
synopsis_list = get_synopsis(movie_id_list)

#this function return a list od bag_of_words
def bag_of_words(string_):
    try:
        all_stopwords = stopwords.words('english')
        text_tokens= [word for word in word_tokenize(string_) if word.isalnum()] 
        bag_of_words = [word for word in text_tokens if not word in all_stopwords]
        filtered_string = [' '.join(bag_of_words)]
            
        return filtered_string
    except TypeError:
        print("passed empty  argument")

#diction creation  with title as key and synopsis as value
movie_data_dict = {}
num = 0
for string_ in synopsis_list:
    new_str = string_.translate(str.maketrans("", "", punctuation))
    movie_data_dict[movie_id_list[num]] =  bag_of_words(new_str)
    num+=1



Omdb_key = "64a6542a" # apikey for OBDb website

# creating a api that return movie data
def fetchting_movie_data(movie_id):
    pattern = r"\D{2}\d{7}"
    try:
        if re.compile(pattern).match(movie_id).group()==movie_id:
            fetched_data = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={Omdb_key}")
            synopsis_data = fetched_data.json()
            return synopsis_data
    except TypeError:
        print("movie_id is not int ")
for movie_id  in movie_id_list:
    response = fetchting_movie_data(str(movie_id))
    try :
        temp_dict = {}
        temp_dict['Synopsis'] = movie_data_dict[f'{movie_id}']
        temp_dict['Genre'] = response['Genre']
        temp_dict['Actors'] = response['Actors']
        movie_data_dict[f'{movie_id}'] =temp_dict
    except KeyError:
        print("key not found")
        
print(movie_data_dict)


fields = ['title','Synopsis','Genre','Actors']
file_name = 'movies_dict_csv.csv'
def dict_to_csv_writer():
    if os.path.exists(file_name):
        file_ = open(file_name,'r')
        file_reader = csv.DictReader(file_)
        for row in file_reader:
            for item in movie_id_list:
                try:
                    if row['title'] == item:
                        movie_data_dict.pop(item)
                except KeyError:
                    print("key not found")
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

dict_to_csv_writer()


def search_movies_data():
    
    user_input = input("Enter Genre or Actors ,keep in mind it is case sensitve!! ")
    if user_input and not user_input.isdigit():
        with open(file_name, 'r') as file_:
            csv_reader = csv.DictReader(file_)
            filtered_data = [row for row in csv_reader if row['Actors']==user_input or row['Genre']==user_input]
            return filtered_data

print(search_movies_data())

    
