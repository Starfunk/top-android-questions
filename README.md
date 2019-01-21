# ANDROIDPHILE
### Keep up to date with the most recent and top-rated android discussions on StackOverflow!

This repository implements a Flask-based website that displays the top and newest questions with an android tag from StackOverflow.

## Installing dependencies
In order to run the project, there are a few dependencies that need to be installed.

* [StackAPI](https://stackapi.readthedocs.io/en/latest/user/intro.html) - The StackOverflow API
* [Flask](http://flask.pocoo.org/) - The webframework used
* [Calendar](https://docs.python.org/2/library/calendar.html) - Used to get number of days in a month
* [Schedule](https://schedule.readthedocs.io/en/stable/) - Used to schedule website updates


On Mac, simply running ```pip install [name of dependency]``` should do the trick. 

## Running the project

1. Navigate to the project folder (on Macs you can use ```cd``` to get into the folder where the files are stored). 

2. Execute ```export FLASK_APP=flask_website.py``` in Terminal.

3. Finally, run the program using ```flask run```.

## Project description

The website, "ANDROIDPHILE", gets its data as a json from StackOverflow using StackAPI. 

The first API returns a json of the top android posts from the last week. 

The second API returns a json of the most recent android posts.

I found the most convenient way of displaying the question thread was simply to have the post titles link to the actual threads on StackOverflow, not only was this more convenient for me but the jsons did not actually contain question thread information so there as no way for me to recreate a question thread on ANDROIDPHILE. 

Since this website is about keeping up to the date with the most-recent and top-rated posts, I added a custom feature which takes the json data and plots the reputation of each of the posters. This way, someone on ANDROIDPHILE can make a choice as to which question they want to look at based on the "quality" of the poster and not just the post itself.  

The website runs using the Flask framework. It is scheduled to auto-update every hour. 
