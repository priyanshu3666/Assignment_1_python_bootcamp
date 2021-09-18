from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests,bs4

def top_movie(url,top_num):
    request_ = requests.get(url)
    soup =bs4.BeautifulSoup(request_.text,'lxml')
    movie_id_list =[]
    for num in range(top_num):
        class_content  = soup.select('.titleColumn')[num]('a')[0]['href']
        movie_id_list.append((str(class_content).split("/"))[2])
    return movie_id_list

#print(top_5_movie("https://www.imdb.com/chart/top/"))

def get_synopsis(movies_id):
    base_url = "https://www.imdb.com/title/"
    synopsis_list = []
    for movie_id in movies_id:
        request_ = requests.get(base_url+movie_id)
        soup = bs4.BeautifulSoup(request_.text,'lxml')
        synopsis = soup.select('.ipc-html-content.ipc-html-content--base')[1]
        synopsis_list.append(synopsis.getText())
    return synopsis_list

movie = top_movie("https://www.imdb.com/chart/top/",1)
synopsis_list = get_synopsis(movie)



def bag_of_words(synopsis_list):
    bag_of_words =[]
    all_stopwords = stopwords.words('english')
    all_stopwords.append(['of','he','a','the','is','the',])
    for content in synopsis_list:        
        text_tokens = new_words= [word for word in word_tokenize(content,language='english') if word. isalnum()] 
        bag_of_words.append([word for word in text_tokens if not word in all_stopwords])
    return bag_of_words




