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

From terminal, use ```cd``` to get into the folder where the files are stored. 

Then execute ```export FLASK_APP=flask_website.py``` in the terminal

Finally, run the program using ```flask run```.

## Project description
