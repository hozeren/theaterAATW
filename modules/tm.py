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

def scrape_tm():

    url = 'https://www.theatermania.com/news'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="styled__CssContentListInfo-sc-2vb2mr-1 khmdNV"]//a/@href')
    print(links)
#we got the content/link above

    for link in links:
        r = requests.get('https://www.theatermania.com'+link, headers=HEADERS)
        #print(r["content"])
        #browser.get(url)
        #blog_tree2 = browser.page_source
        blog_tree = fromstring(r.content)
        #print html.tostring(blog_tree)
        #print(blog_tree)
        #paras = browser.find_element_by_xpath("//*[@id='content-container']/div[4]/main/article/div[4]//p/text()")
        paras = blog_tree.xpath(u'//*[@id="content-container"]/div[4]/main/article/div[4]//p') #encode('utf8')
        print(paras)
        stop
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s %s' % (text.encode('utf-8'), "@theatermania", 'https://www.theatermania.com'+link) #for the loop which may be stuck
    
    '''put the url behind if href is not full'''

def main():
    """Encompasses the main loop of the bot."""
    print('----Bot started.----')
    news_funcs = ['scrape_tm']
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
            except StopIteration:
                news_iterators[i] = globals()[news_funcs[i]]()


if __name__ == "__main__":  
    para = []
    paras = []
    e = Extract(para, paras)
    main()


