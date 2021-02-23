
#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk
nltk.download('punkt')
import requests
import sys
from twython import Twython, TwythonError

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work

from auth import (
    apiKey,
    apiSecret,
    accessToken,
    accessTokenSecret
)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
    }

def extract_paratext(paras):
    """Extracts text from <p> elements and returns a clean, tokenized random
    paragraph."""

    paras = [para.text_content() for para in paras if para.text_content()]
    para = random.choice(paras)
    return tokenizer.tokenize(para)

def extract_text(para):
    """Returns a sufficiently-large random text from a tokenized paragraph,
    if such text exists. Otherwise, returns None."""

    for _ in range(10):
        text = random.choice(para)
        if text and 60 < len(text) < 210:
            return text

    return None

def scrape_nytimes():

    url = 'https://www.nytimes.com/section/theater'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links1 = tree.xpath('//h2[@class="css-171kk9w e4e4i5l1"]/a/@href')
    links2 = tree.xpath('//div[@class="css-1l4spti"]/a/@href')
    links = links2+links1

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