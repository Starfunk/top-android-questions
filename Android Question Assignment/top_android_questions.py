""" A program that interfaces with StackAPI and returns StackOverflow's 
top and newest android questions from the past week"""

from stackapi import StackAPI
from datetime import datetime, date, timedelta
import calendar

"""Implements the StackOverflow object which contains the 10 top-rated questions
and the most recently-posted questions, which are tagged as "android"""
class StackOverflow:
	
	def __init__(self):
		SITE = StackAPI('stackoverflow')		
		# Number of items per page
		SITE.page_size = 10
		# Number of api calls
		SITE.max_pages = 1
		# Get the current date and time as a datetime object
		self.date = datetime.now()
		# Get dates for thepast week where first day of the week is Monday(0)
		# and last day of the week is Sunday (6)
		interval = self.past_week()
		# Get the top-rated android questions from the past week
		self.top = SITE.fetch('questions', fromdate=interval[0], 
			todate=interval[1], sort='votes', tagged='android')['items']
		# Get the most recent android questions
		self.new =  SITE.fetch('questions', sort='creation', 
			order='desc', tagged='android')['items']
 
	# Returns an array containing the start and end dates as datetime objects 
	# of the past week
	def past_week(self):
		# Get the current date
		day, month, year = self.date.day, self.date.month, self.date.year
		# Get the current weekday
		weekday = self.date.weekday()
		endday, endmonth, endyear = get_last_week(day, month, year, 
			weekday, True)
		enddate = date(endyear, endmonth, endday)
		startday, startmonth, startyear = get_last_week(endday, 
			endmonth, endyear, enddate.weekday(), False)
		startdate = date(startyear, startmonth, startday)
		return ([startdate, enddate])


# There are many ways to define "past week", I define a week as starting on 
# Monday and ending on Sunday. This is a helper function for past_week
def get_last_week(day, month, year, weekday, flag):
	# If counter = 1 then we are looking at the last day of last week, otherwise
	# day - weekday gives the date of the first day of the week.
	counter = 0
	if flag:
		counter = 1	
	# If last week was in previous month
	if day - weekday < 1:
		# If last week was in previous year
		if month - 1 < 1:	
			year = year - 1
			month = 12
			day = day + 31 - weekday - counter		
		else: 
			# If day is a Monday, then weekday is 0 and the 
			# end of the previous week is (day - 1)
			month = month - 1
			# Get number of days in month
			days_in_month = calendar.monthrange(year, month)[1]
			# Add the date with how many days in previous month and subtract
			# the weekday (-1 since monday is 0) to get the date of the last
			# Sunday
			day = day + days_in_month - weekday - counter
	else: 
		day = day - weekday	- counter
		
	return(day, month, year)
	
	
	
