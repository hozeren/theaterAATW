#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk
nltk.download('punkt', quiet=True)
import sys, requests

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"

class Extract:
    
    def __init__(self,para,paras):
        self.para = para
        self.paras =paras

    def extract_paratext(self, paras):
        """Extracts text from <p> elements and returns a clean, tokenized random
        paragraph."""

        paras = [para.text_content() for para in paras if para.text_content()]
        para = random.choice(paras)
        return nltk.data.load('tokenizers/punkt/english.pickle').tokenize(para)

    def extract_text(self, para):
        """Returns a sufficiently-large random text from a tokenized paragraph,
        if such text exists. Otherwise, returns None."""

        for _ in range(10): #choosing 10 text from the article
            text = random.choice(para)
            if text and 60 < len(text) < 180:
                return text

        return text
