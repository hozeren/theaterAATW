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
- [@TheaterAATW: &quot;Marking the UK theatrical premiere of the stage musical, the production will be directed by Joseph Houston &lpar;he/him&rpar;, with William Whelton &lpar;he/him&rpar; co-directing and choreographing.&quot; @WhatsOnStage](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a26978dc170b9164d360e0ca1a72138239)
- [@TheaterAATW: &quot;This post was written by the author in their personal capacity.The opinions expressed in this article are the author’s own and do not reflect the view of The Theatre Times, their staff or collaborators.&quot; @TheTheatreTimes](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a26978df15069168d569e2c31a7b1d8932)
- [@TheaterAATW: &quot;It is a more appropriate visual metaphor than the creators might realize.&quot; @theatermania](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a26978df140a9464d169e1c4167e118b33)
- [@TheaterAATW: &quot;Also on Tuesday, Trinity Irish Dance Company begins a run through March 20 at the Joyce Theater in Manhattan &lpar;tickets start at $20 at &rpar;.BRIAN SCHAEFER&quot; @nytimestheater](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a26978df140e9b68d36be8c7117e158b3d)
- [@TheaterAATW: &quot;The creative team remains as-is, with casting for the new run are to be revealed.&quot; @WhatsOnStage](https://rss.app/articles/cb4e791f6f6d729c074351566bd3a7c508111d6e2b37b7e0d6e7953ba4b25088f10ba4482c9bc169f6a26979d71c0e9161dc68e2c5177e168d3f)
<!-- TWITTER:END -->
