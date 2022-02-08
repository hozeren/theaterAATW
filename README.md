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
usage: theateraatw [-h] [nytimes] [wostage] [tmania] [ttimes]

positional arguments:
  nytimes     Start scraping and sending tweets from New York Times.
  wostage     Start scraping and sending tweets from WhatsOnStage.
  tmania      Start scraping and sending tweets from TheaterMania.
  ttimes      Start scraping and sending tweets from The Theatre Times.

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
- [@TheaterAATW: &quot;The cast also includes Jewelle Blackman, Jessie Shelton, and Kay Trinidad as the Fates, and Lana Gordon as the Persephone alternate.&quot; @theatermania](https://twitter.com/TheaterAATW/status/1490832115248037890)
- [@TheaterAATW: &quot;Jane Lynch will play Mrs. Rose Brice and Jared Grimes will play Eddie Ryan.&quot; @WhatsOnStage](https://twitter.com/TheaterAATW/status/1490832043734966278)
- [@TheaterAATW: &quot;This would be unsurprising for a drama written in the 1960s or 1970s, but for a 1999 play it’s a touch woeful.&quot; @TheTheatreTimes](https://twitter.com/TheaterAATW/status/1490831992400883714)
- [@TheaterAATW: &quot;The MoMA favorite “Her Man,” with Twelvetrees, screens on Sunday and Feb. 17.BEN KENIGSBERG&quot; @nytimestheater](https://twitter.com/TheaterAATW/status/1490831891515293701)
- [@TheaterAATW: &quot;&lpar;Families seeking access to both on-site and online events must purchase admission separately.&quot; @nytimestheater](https://twitter.com/TheaterAATW/status/1490831403029868545)
<!-- TWITTER:END -->
