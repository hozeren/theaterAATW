#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt', quiet=True)
from twython import Twython, TwythonError
import sys, requests


class Favorite():


    def search_twitter(keywords):
        results = twitter.cursor(twitter.search, q=keywords)
        for result in results:
        print(result['id_str'])
        return results

    def 