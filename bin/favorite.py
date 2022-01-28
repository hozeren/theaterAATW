#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt', quiet=True)
from twython import Twython, TwythonError
import sys, requests
from theaterAATW.auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

keywords = ['theater']
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

class Favorite():


    def search_twitter(keywords):
        results = api.cursor(api.search, q=keywords)
        for result in results:
            print(result['id_str'])
            return results

Favorite()
print (Favorite.search_twitter(keywords))
