#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt', quiet=True) 
from twython import Twython, TwythonError
from ..bin.extract import Extract
from ..auth2 import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret,
    HEADERS
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"

def scrape_wostage():
    para = []
    paras = []
    e = Extract(para, paras)
    url = 'https://www.whatsonstage.com/news?categories=theatre-news'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath(u'//div[@class=" article-loop-container"]//a/@href')
    random.shuffle(links) #shuffle the list for more randomization
    #print(links)
    
    #we got the content/link above

    for link in links:
        print(link)
        r2 = requests.get(link, headers=HEADERS)
        blog_tree = fromstring(r2.content)
        paras = blog_tree.xpath('//div[@class="entry-content"]//p')
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s %s' % (text, "@WhatsOnStage", link) #for the loop which may be stuck
    #return link
    
    '''put the url behind if href is not full'''
