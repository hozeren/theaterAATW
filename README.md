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
- [&quot;“Nero.” PC: Molnár Edvárd.&quot; @TheTheatreTimes](https://x.com/TheaterAATW/status/1615951653269544961)
- [&quot;Blankson-Wood appeared as Orlando in last season&#39;s production of As You Like It, which featured music by Shaina Taub and a giant chorus.&quot; @theatermania](https://x.com/TheaterAATW/status/1615951043690467328)
- [&quot;The bio-musical, which boasts such classics as &quot;That&#39;ll Be The Day&quot;, &quot;Peggy Sue&quot; and &quot;Oh Boy&quot;, charts the rockabilly singer&#39;s rise to fame until his untimely death at the age of 22.&quot; @WhatsOnStage](https://x.com/TheaterAATW/status/1615950822717952001)
- [&quot;Backing into writing after a stint at the Asiatic Petroleum Company, his macabre voice and flights into fantasy were clearly engendered by brushes with death and violence.&quot; @nytimestheater](https://x.com/TheaterAATW/status/1615918631413583874)
- [&quot;This post was written by the author in their personal capacity.The opinions expressed in this article are the author’s own and do not reflect the view of The Theatre Times, their staff or collaborators.&quot; @TheTheatreTimes](https://x.com/TheaterAATW/status/1615906351384825856)
<!-- TWITTER:END -->
