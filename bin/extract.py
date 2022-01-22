#!/usr/bin/env python
import random
import time

from lxml.html import fromstring
import nltk
nltk.download('punkt', quiet=True)
import requests
import sys



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

        for _ in range(10):
            text = random.choice(para)
            if text and 60 < len(text) < 210:
                return text

        return text
