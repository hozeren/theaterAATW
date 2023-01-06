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
- [@TheaterAATW: &quot;With a bookshelf, murals and seats that fold into the walls, the space is meant for any form of workshops, performances and even rehearsals.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f5a36a7ad7120d9162d061e1c1147e138b3b)
- [@TheaterAATW: &quot;Marla Mindelle leads the cast as Céline, a starry-eyed romantic who claims to have been there on that fateful night.&quot; @theatermania](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f5a36a7ad7120e9562d16ce5c2177312893c)
- [@TheaterAATW: &quot;– Good will start at 1.30pm on 24 December &lpar;rather than the previously announced 2.30pm&rpar; because of the strike.&quot; @WhatsOnStage](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f5a36a7ad7120e9060d66be3c61772148a39)
- [@TheaterAATW: &quot;That is, when Johnson wasn’t glued to “Murder, She Wrote,” the cozy CBS series that cast Lansbury as the crime-solving author Jessica Fletcher.&quot; @nytimestheater](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f5a36a7ad8130d9769d361e8c2167e178c3d)
- [@TheaterAATW: &quot;This post was written by Ati Metwaly.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f5a36a7adb14069263d46ce6c1167d1d8e33)
<!-- TWITTER:END -->
