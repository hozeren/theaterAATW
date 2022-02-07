#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt', quiet=True)
from twython import Twython, TwythonError
from theaterAATW.bin.extract import Extract
import sys, requests
from theaterAATW.auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

#keywords = ['theater']
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

class Outbound():
    def __init__(self, keywords):
        self.keywords = keywords


    def search_twitter(self):
        results = api.cursor(api.search, q=self.keywords)
        for result in results:
            print(result['id_str'])
            return results

#a = Favorite(keywords)
#print (a.search_twitter())
