#!/usr/bin/env python
import random
import time

import sys, requests
from twython import Twython, TwythonError
from theaterAATW.bin.extract import Extract
import sys, requests
from random import randint
from theaterAATW.auth2 import (
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
                a = randint(600, 3600)
                print('------ We will wait for ' + str(round(a / 60, 0)) + ' min for the next like. ------')
                time.sleep(a)
            except (StopIteration, IndexError, TwythonError):
                pass

