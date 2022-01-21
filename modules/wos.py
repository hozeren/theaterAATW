#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt') 
from twython import Twython, TwythonError
from theaterAATW.src.extract import Extract
from theaterAATW.auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

def scrape_wostage():

    url = 'https://www.whatsonstage.com/news?categories=theatre-news'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="styled__CssContentListInfo-sc-2vb2mr-1 khmdNV"]/a/@href')
    
#we got the content/link above

    for link in links:
        r = requests.get('https://www.whatsonstage.com'+link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paras = blog_tree.xpath('//div[@class="BodyContent-sc-1r3al1a-0 styled__CssArticleBody-asi60b-13 eTxOCF"]//p')
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s' % (text, 'https://www.whatsonstage.com'+link) #for the loop which may be stuck
    
    '''put the url behind if href is not full'''

def main():
    """Encompasses the main loop of the bot."""
    print('----Bot started.----')
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
    para = []
    paras = []
    e = Extract(para, paras)
    main()

