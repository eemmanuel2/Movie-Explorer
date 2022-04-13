## Setup Instructions
1. `pip3 install -r requirements.txt`
2. Create a `.env` file in the top-level directory and enter the following as its contents:
```
export TMDB_API_KEY="<YOUR API KEY>"
export DATABASE_URL="<YOUR POSTGRESQL DB URL>"
```



## To run the app
1. run `npm run build`
2. Run `python3 routes.py`



# The Movie Explorer
A simple web-app that displays a different movie (4 of my favorite movies to be exact) each time the page is refreshed along side it's wikipedia page. This app has an added feature where you will be able to sign up and register to rate the movie and give a comment of your own! A new added feature lets you edit/delete your comments/rate at any time. This will give you a much more flexible approach to the user experience 

## How was it created?
This app was created in python using functionalities such as Flask, Html, Css, SQLAlchemy, Javascript, and etc. The APIs used here were TMDB's API and Wikipedia's API.

## Some challenges
I've had my ups and downs with this milestone 3 (alot of downs) but I ended up making a respectable web-application. I've had more than three technical issues but my biggest ones were: 
1. Having my json data display on my app.js page. This was very hard for me and I didn't figure it out till today honestly. I just added my whole URL into the `fetch` request and it worked. Also changed it from a `.json` to a `.text`
2. Impleneting a delete button was a very difficult task for me. But it does completely delete the rating 100% out of the database. I figured this out through youtube and lots of stressful moments I figured out how to do this.

## <b> Finally </b> 
The hardest part of this project was definetely this one. Javascript/react is so foreign to me that I almost had no idea what I was doing till only a couple days ago and my brain finally clicked. The most useful thing I've learned is just everything that we've done. I've walked into this course with 0 Knowledge of Python,Flask,Heroku,JavaScript,React. And now I'm walking out with tons of knowledge and familarities around these programs, might not be the best but I'm extremely proud of what I've accomplished so far. 
Thank You!


Heroku URL : https://mighty-spire-29615.herokuapp.com/

Please Enjoy :) !!

- Edwin Emmanuel

## Setup Instructions
1. `pip3 install -r requirements.txt`
2. Create a `.env` file in the top-level directory and enter the following as its contents:
```
export TMDB_API_KEY="<YOUR API KEY>"
export DATABASE_URL="<YOUR POSTGRESQL DB URL>"
```



## To run the app
1. run `npm run build`
2. Run `python3 routes.py`



