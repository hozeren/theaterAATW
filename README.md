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
- [@TheaterAATW: &quot;The world premiere of &#39;When Playwrights Kill&#39;&#39;, which had been scheduled for the Bushnell&#39;s Belding Theatre in Hartford, Connecticut July 26 - August 7, has been postponed.&quot; @theatermania](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a1637ada120c9363dd6ce8c21a791c8339)
- [@TheaterAATW: &quot;The recurrence of certain devices – a static camera, recurring images, filming in black and white – becomes meaningful when we consider that the pieces are intended to form a whole.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a1637ada120e9a68d768e3cb177813883f)
- [@TheaterAATW: &quot;&quot;That said, we will not compromise on safety and the strike does mean that large parts of the network will be closed.&quot;&quot; @WhatsOnStage](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a1637ada10089a68d76be7c6167912893e)
- [@TheaterAATW: &quot;“We began with looking for the differences between us, but at some point we came to realize that we were so similar.”–Kasper Daugård Poulsen&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a1637ade14079a65d268e4c41a7d148a32)
- [@TheaterAATW: &quot;A West End transfer would follow in the autumn of 2019, which also took home the Olivier Award for &#39;Best New Musical&#39;.&quot; @theatermania](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a1637adf1d069a68d56be7c4147f178939)
<!-- TWITTER:END -->
