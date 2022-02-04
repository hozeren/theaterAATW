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
- [@TheaterAATW: &quot;The success of this approach prompted Scottish students taking part to ask themselves what objects and locations from their own culture could be used in their adaptations of Shakespeare’s Pericles.&quot; @TheTheatreTimes](https://twitter.com/TheaterAATW/status/1489355129304268800)
- [@TheaterAATW: &quot;As the Arts Council has flagged in recent reports, local government is the largest investor in the arts and culture sector in England.&quot; @WhatsOnStage](https://twitter.com/TheaterAATW/status/1489354996063875075)
- [@TheaterAATW: &quot;Lighting by Martha Godfrey and sound design by Christ Whybrow.&quot; @theatermania](https://twitter.com/TheaterAATW/status/1489354848839643136)
- [@TheaterAATW: &quot;Collegiality, scorn, fear, affection — and a shared history saved for a late reveal — all come into it.&quot; @nytimestheater](https://twitter.com/TheaterAATW/status/1489354578600603655)
- [@TheaterAATW: &quot;“The Nutcracker,” performed at the Cairo Opera House’s main hall, by the Cairo Opera Ballet Company.&quot; @TheTheatreTimes](https://twitter.com/TheaterAATW/status/1489309826698076169)
<!-- TWITTER:END -->
