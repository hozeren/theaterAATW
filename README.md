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
- [@TheaterAATW: &quot;This article was posted by Aleks Sierz on January 14, 2022, and has been reposted with permission.&quot; @TheTheatreTimes](https://twitter.com/TheaterAATW/status/1488856614992031745)
- [@TheaterAATW: &quot;The musical director is Jennifer Deacon and UK musical supervisor is Katy Richardson.&quot; @WhatsOnStage](https://twitter.com/TheaterAATW/status/1488856592346931205)
- [@TheaterAATW: &quot;It also features Jonathan Nieves as Richie, Jason Schmidt as Buddy, Maxwell Whittington-Cooper as Wally, and Jackie Hoffman as Assistant Principal McGee.&quot; @theatermania](https://twitter.com/TheaterAATW/status/1488856503499042817)
- [@TheaterAATW: &quot;Rivera, who turned 89 this month, has done career retrospectives before, including “The Dancer’s Life,” a musical celebrating her career.&quot; @nytimestheater](https://twitter.com/TheaterAATW/status/1488856251933020161)
- [@TheaterAATW: &quot;This is an argument about the past and progress, and it reflects some of the real-life attitudes that continue to affect the popularity of tap, especially among Black people, and the potential pool of tap dance kids.&quot; @nytimestheater](https://twitter.com/TheaterAATW/status/1488817189251596289)
<!-- TWITTER:END -->
