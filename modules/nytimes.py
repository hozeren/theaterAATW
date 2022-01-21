#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt') 
from twython import Twython, TwythonError
from ..lib import extract
from auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

def scrape_nytimes():

    url = 'https://www.nytimes.com/section/theater'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links1 = tree.xpath('//h2[@class="css-171kk9w e4e4i5l1"]/a/@href')
    links2 = tree.xpath('//div[@class="css-1l4spti"]/a/@href')
    links = links2+links1
    print(links)

#we got the content/link above

    for link in links:
        r = requests.get('https://www.nytimes.com'+link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paras = blog_tree.xpath('//div[@class="css-53u6y8"]/p')
        para = extract_paratext(paras)
        text = extract_text(para)
        if not text:
            continue

        yield '"%s" %s' % (text, 'https://www.nytimes.com'+link) #for the loop which may be stuck
    
    '''put the url behind if href is not full'''

def main():
    """Encompasses the main loop of the bot."""
    print('----Bot started.----')
    news_funcs = ['scrape_nytimes']
    news_iterators = []  
    for func in news_funcs:
        news_iterators.append(globals()[func]())
    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                api.update_status(status=tweet)
#                print(tweet)
                time.sleep(10800) 
            except (StopIteration, IndexError): #fix index error cf line 37
                news_iterators[i] = globals()[news_funcs[i]]()


if __name__ == "__main__":  
    main()