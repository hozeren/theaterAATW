#!/usr/bin/env python
import random
import time

import sys, requests
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
                time.sleep(1200)
            except (StopIteration, IndexError, TwythonError):
                

