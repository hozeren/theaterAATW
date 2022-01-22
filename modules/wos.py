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
    para = []
    paras = []
    e = Extract(para, paras)
    url = 'https://www.whatsonstage.com/news?categories=theatre-news'
    r = requests.get(url, headers=HEADERS).json()
    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="styled__CssContentListInfo-sc-2vb2mr-1 khmdNV"]/a/@href')
    
#we got the content/link above

    for link in links:
        r = requests.get('https://www.whatsonstage.com'+link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paras = blog_tree.xpath('//h1[@itemprop="name"]//p')
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s' % (text, 'https://www.whatsonstage.com'+link) #for the loop which may be stuck
    
    '''put the url behind if href is not full'''


