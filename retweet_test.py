#!/usr/bin/env python
import sys
from twython import Twython, TwythonError
import random

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work

from auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

vital = ["theater","acting"]
city = [" London"," New York"," Stockholm"," Berlin"," News"]

try:
        if len(vital) > 0:
            Vital  = random.choice(vital)
	    City = random.choice(city)
	    keywords = Vital+City
	    print(keywords)
#Setting Twitter's search keywords randomly will be chosen.
#q= is important here! keyword function can be tailor-made
	    search_results = api.search(q=keywords, count=1, lang="en", result_type="popular")
            for tweet in search_results["statuses"]:
                api.retweet(id = tweet["id_str"])
        else:
            print("Loop Error!")
except TwythonError as Error:
      print Error
