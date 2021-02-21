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
search_results = api.search(q="#theater", count=1, result_type="popular")
try:      
#Setting Twitter's search keywords randomly will be chosen.
#q= is important here! keyword function can be tailor-made

            for tweet in search_results["statuses"]:
                print(tweet)
                api.retweet(id = tweet["id_str"])

except TwythonError as Error:
      print Error
