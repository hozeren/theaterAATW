Theater All Around the World
========

A Twitter bot that posts scrapped text and links from specified theater websites on Twitter without the intervention of a human operator.

<p align="center">
<img src="theaterAATW_logo.png"  alt="TheaterAATW" width="40%">
</p>
<p align="center">

## Installation
  Before installation, `auth.py` should be filled and/or created with the Twitter API key and secret in the main folder. You can apply to Twitter developer account below:
  https://developer.twitter.com/
  
  ```bash
  # Clone the repositories
  git clone https://github.com/hozeren/theaterAATW.git
  
  # Go to the clone folder
  python setup.py install
  
  # or install with pip in the folder
  pip install .
  ```
## Usage
  There are two website functions now including [New York Times](https://www.nytimes.com/section/theater), [Whatsonstage](https://www.whatsonstage.com/news/?categories=theatre-news), [The Theatre Times](https://thetheatretimes.com/featured/), and [TheaterMania](https://www.theatermania.com/news/). To use the functions after installation;
  ```bash
usage: theateraatw [-h] [nytimes] [wostage] [tmania] [ttimes] [fav]

positional arguments:
  nytimes     Start scraping and sending tweets from New York Times.
  wostage     Start scraping and sending tweets from WhatsOnStage.
  tmania      Start scraping and sending tweets from TheaterMania.
  ttimes      Start scraping and sending tweets from The Theatre Times.
  fav         Favorite the tweets, use with following keywords.

optional arguments:
  -h, --help  show this help message and exit
  ```
## Tweet on Twitter
  
<p align="center">
<a href="https://twitter.com/TheaterAATW/status/1488766001269420034"><img src="example-tweet.png"  alt="TheaterAATW" width="50%">
</p>
<p align="center">

### 📱 Latest Tweets

<!-- TWITTER:START -->
- [@TheaterAATW: &quot;Viviani per strada.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6ab6d7ddd10099461d060e5ca1573118239)
- [@TheaterAATW: &quot;Five years ago, David Cale&#39;s Harry Clarke enjoyed a successful run off-Broadway in a production starring Billy Crudup as a man leading a double life.&quot; @theatermania](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6ab6d7ddd100a9b61dd6ce6c51472148333)
- [@TheaterAATW: &quot;Lead casting has been set for the upcoming new play The Motive and the Cue, running at the National Theatre from April.&quot; @WhatsOnStage](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6ab6d7ddd100b9660d169e5c4147a128839)
- [@TheaterAATW: &quot;For little over an hour, the actresses Sandra Gerling, Josefine Israel and Sasha Rau perform around, under and on top of Park’s massive sculpture.&quot; @nytimestheater](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6ab6c74d614089168d36ae0c4177f148a32)
- [@TheaterAATW: &quot;“I was acting in Paris in 2019 in the late Yukio Ninagawa’s wonderful adaptation of Haruki Murakami’s novel ‘Kafka on the Shore,’” Kakizawa recalls.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6ab6c74d81d0c9561d56de4c11b721d883d)
<!-- TWITTER:END -->
