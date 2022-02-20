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

keywords = ['theater']
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

class Outbound():
    def __init__(self, keywords):
        self.keywords = keywords

    def favorite_twitter(self):
        results = api.cursor(api.search, q=self.keywords)
        for result in results:
            try:
                api.create_favorite(id=result['id'])
                print("Bot liked: "+result['text'])
                sleep(1200)
            except (StopIteration, IndexError, TwythonError):
                stop

a = Outbound(keywords)
a.favorite_twitter()

