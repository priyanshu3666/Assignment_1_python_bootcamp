FROM python:3
ADD . .
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
CMD ["web_scrapper.py"]
ENTRYPOINT [ "python3" ]
