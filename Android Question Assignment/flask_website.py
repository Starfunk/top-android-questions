""" Implements a Flask-based website that shows the top-rated and 
most recent android related posts on StackOverflow """

from flask import Flask, render_template
from top_android_questions import StackOverflow
import time
import schedule

# Creating Flask instance
app = Flask(__name__)

# Create a new instance of StackOverflow, this creates two API calls
# and gets the most recent post data from StackOverflow
questions = StackOverflow()

# Store names and reputation to use in scatter plots
newnames = []
topnames = []
newrep = []
toprep = []

for i, j in zip(questions.new, questions.top):
	newnames.append(i['owner']['display_name'])
	topnames.append(j['owner']['display_name'])
	
for i, j in zip(questions.new, questions.top):
	newrep.append(i['owner']['reputation'])
	toprep.append(j['owner']['reputation'])

# Defining the homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', newquestions=questions.new,
		topquestions=questions.top, topnames=topnames, newnames=newnames,
		toprep=toprep, newrep=newrep)

if __name__ == '__main__':
	
	# Schedule to run an update (i.e. call StackOverflow())
	schedule.every().second.do(app.run)
	while True:
		schedule.run_pending()
		time.sleep(10)
