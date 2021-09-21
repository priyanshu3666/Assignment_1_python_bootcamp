FROM python:3
ADD . .
RUN pip3 install lxml
RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install nltk
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
CMD ["web_scraping_unit_testing.py"]
ENTRYPOINT [ "python3" ]
