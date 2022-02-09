#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk, sys, requests
nltk.download('punkt', quiet=True) 
from twython import Twython, TwythonError
from theaterAATW.bin.extract import Extract
from theaterAATW.auth import (
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

def scrape_tmania():
    para = []
    paras = []
    e = Extract(para, paras)
    url = 'https://www.theatermania.com/news'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath('//a[@class="styled__CssContentLinkTitle-sc-2vb2mr-2 fqiVOp"]//@href')
    random.shuffle(links) #shuffle the list for more randomization

#we got the content/link above

    for link in links:
        r = requests.get('https://www.theatermania.com'+link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paras = blog_tree.xpath(u'//div[@itemprop="articleBody"]//p') #encode('utf8')
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s %s' % (text, "@theatermania", 'https://www.theatermania.com'+link) #for the loop which may be stuck
    
    '''put the url behind if href is not full'''



