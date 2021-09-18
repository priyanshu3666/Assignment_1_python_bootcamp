from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests,bs4
import re
def top_movie(url,top_num):
    request_ = requests.get(url)
    soup =bs4.BeautifulSoup(request_.text,'lxml')
    movie_id_list =[]
    for num in range(top_num):
        class_content  = soup.select('.titleColumn')[num]('a')[0]['href']
        movie_id_list.append((str(class_content).split("/"))[2])
    return movie_id_list



def get_synopsis(movies_id):
    base_url = "https://www.imdb.com/title/"
    synopsis_list = []
    for movie_id in movies_id:
        request_ = requests.get(base_url+movie_id)
        soup = bs4.BeautifulSoup(request_.text,'lxml')
        synopsis = soup.select('.ipc-html-content.ipc-html-content--base')[1]
        synopsis_list.append(synopsis.getText())
    return synopsis_list

movie_id_list = top_movie("https://www.imdb.com/chart/top/",1)
synopsis_list = get_synopsis(movie_id_list)



def bag_of_words(synopsis_list):
    bag_of_words =[]
    all_stopwords = stopwords.words('english')
    all_stopwords.append(['of','he','a','the','is','the',])
    for content in synopsis_list:        
        text_tokens = new_words= [word for word in word_tokenize(content,language='english') if word. isalnum()] 
        bag_of_words.append([word for word in text_tokens if not word in all_stopwords])
    return bag_of_words


def movie_dict(movie_id_list,synopsis_list):
    movies_dict = {}
    for movie_id in movie_id_list:
        for value in synopsis_list:
            movies_dict[f'{movie_id}'] = value
    print(movies_dict)

movie_dict(movie_id_list,synopsis_list)


Omdb_key = "64a6542a"

def fetchting_movie_data(movie_id):
    pattern = r"\D{2}\d{7}"
    if re.compile(pattern).match(movie_id).group()==movie_id:
        fetched_data = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={Omdb_key}")
        synopsis_data = fetched_data.json()
        return synopsis_data
for movie_id  in movie_id_list:
    fetchting_movie_data(str(movie_id))