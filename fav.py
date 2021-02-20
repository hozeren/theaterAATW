#!/usr/bin/env python
import sys
from twython import Twython, TwythonError, TwythonRateLimitError
import random
import time
import requests

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work

from auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret
)

while True:
    try:      
#Setting Twitter's search keywords randomly will be chosen.
#q= is important here! keyword function can be tailor-made
        api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
        search_results = api.cursor(api.search,q= "#theater", result_type="recent")

        for tweet in search_results: #["statuses"] new code for twyton
            print("Liked!: %s" % tweet["text"])
            #print(tweet["id_str"]) 
            api.create_favorite(id = tweet["id_str"])
            #time.sleep(240)                
            
#except TwythonError as Error:
 #   print Error
    except TwythonRateLimitError, e:
         print "[Exception Raised] Rate limit exceeded"
         reset = int(api.get_lastfunction_header('x-rate-limit-reset'))
         print(reset)
         wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
         print(wait)
         time.sleep(wait)
    except Exception, e:
         print e
         print "Non rate-limit exception encountered. Sleeping for 15 min before retrying"
         time.sleep(60*15)