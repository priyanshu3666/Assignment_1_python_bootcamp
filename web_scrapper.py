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

movie_id_list = top_movie("https://www.imdb.com/chart/top/",1)
synopsis_list = get_synopsis(movie_id_list)

#this function return a list od bag_of_words
def bag_of_words(string_):
    
    all_stopwords = stopwords.words('english')
    
    for content in synopsis_list:       
        text_tokens= [word for word in word_tokenize(content) if word.isalnum()] 
        bag_of_words = [word for word in text_tokens if not word in all_stopwords]
        filtered_string = [' '.join(bag_of_words)]
        
    return filtered_string


movie_data_dict = {}
num = 0
for string in synopsis_list:
    my_punctuation = punctuation.replace("'", "")
    new_str = string.translate(str.maketrans("", "", my_punctuation))
    movie_data_dict[movie_id_list[num]] =  bag_of_words(new_str)
    num+=1



Omdb_key = "64a6542a"

# creating a api that return movie data
def fetchting_movie_data(movie_id):
    pattern = r"\D{2}\d{7}"
    if re.compile(pattern).match(movie_id).group()==movie_id:
        fetched_data = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={Omdb_key}")
        synopsis_data = fetched_data.json()
        return synopsis_data
for movie_id  in movie_id_list:
    response = fetchting_movie_data(str(movie_id))
    temp_dict = {}
    temp_dict['Synopsis'] = movie_data_dict[f'{movie_id}']
    temp_dict['Genre'] = response['Genre']
    temp_dict['Actors'] = response['Actors']
    movie_data_dict[f'{movie_id}'] =temp_dict
print(movie_data_dict)
