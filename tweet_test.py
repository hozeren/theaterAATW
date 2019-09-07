#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Welcome!"

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work

from auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
