#!/usr/bin/env python
import pytest
from modules.nytimes import scrape_nytimes
from modules.wostage import scrape_wostage
from modules.tmania import scrape_tmania
from modules.ttimes import scrape_ttimes

def test_scrape_nytimes():
    nytimes_text = scrape_nytimes()
    for text in nytimes_text:
        assert text, "New York Times texts works!"

def test_scrape_wostage():
    wostage_text = scrape_wostage()
    for text in wostage_text:
        assert text, "Wostage texts works!"

def test_scrape_mania():
    texts = scrape_tmania()
    for text in texts:
        assert text, "TheaterMania texts works!"

def test_scrape_ttimes():
    texts = scrape_tmania()
    for text in texts:
        assert text, "TheaterMania texts works!"
