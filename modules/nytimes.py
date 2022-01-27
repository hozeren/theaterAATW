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

def scrape_nytimes():
    para = []
    paras = []
    e = Extract(para, paras)
    url = 'https://www.nytimes.com/section/theater'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links1 = tree.xpath('//h2[@class="css-171kk9w e4e4i5l1"]/a/@href')
    links2 = tree.xpath('//div[@class="css-1l4spti"]/a/@href')
    links = links2+links1
    #print(links)

    #we got the content/link above

    for link in links:
        r2 = requests.get('https://www.nytimes.com'+link, headers=HEADERS)
        blog_tree = fromstring(r2.content)
        paras = blog_tree.xpath('//div[@class="css-53u6y8"]/p')
        para = e.extract_paratext(paras)
        text = e.extract_text(para)
        if not text:
            continue

        yield '"%s" %s %s' % (text, "@nytimestheater", 'https://www.nytimes.com'+link) #this makes the return an object, use "for" loop to see.
    
    '''put the url behind if href is not full'''

