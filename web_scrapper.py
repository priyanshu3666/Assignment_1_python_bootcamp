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


