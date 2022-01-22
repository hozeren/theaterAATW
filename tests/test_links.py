#!/usr/bin/env python
import pytest
from theaterAATW.modules.nytimes import scrape_nytimes
from theaterAATW.modules.wostage import scrape_wostage

def test_scrape_nytimes():
    nytimes_text = scrape_nytimes()
    for text in nytimes_text:
        assert text, "New York Times texts works!"

def test_scrape_wostage():
    wostage_text = scrape_wostage()
    for text in wostage_text:
        assert text, "Wostage texts works!"