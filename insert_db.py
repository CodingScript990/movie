import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)

movie_db = client.dbmovie

# DB movie info insert
def movie_db_insert():
    movie_db.naver.delete_many({})

    for movie in movie_db():
        movie_db.insert_one(movie)

movie_db_insert()