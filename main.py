#!/usr/bin/env python

import random
import time
from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt') 

from theaterAATW.src.extract import Extract
from theaterAATW.modules.nytimes import scrape_nytimes
from theaterAATW.modules.wostage import scrape_wostage
from twython import Twython, TwythonError
from theaterAATW.auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)


def main():
    """Encompasses the main loop of the bot."""
    print('-------Bot started.-------')
    news_funcs = ['scrape_wostage']
    news_iterators = []  
    for func in news_funcs:
        news_iterators.append(globals()[func]())
    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                api.update_status(status=tweet)
                print(tweet)
                time.sleep(10800) 
            except (StopIteration, IndexError): #fix index error cf line 37
                news_iterators[i] = globals()[news_funcs[i]]()

if __name__ == "__main__":  
    main()