#!env/bin/python

###
# Created by: Patric Fox ( patric[dot]fox[at]onelogin[dot]com )
# Date: 04/27/2015
###

###
# requires requests library
###


import requests

###
# Specify the account API Key
###

api_key = ""


def fetchEvents(api_key):
	###
	# download last 50 events
	###
	events = []
	newSession = requests.Session()
	headers = {'Content-Type':'application/xml'}
	target = "https://api.onelogin.com/api/v1/events/"
	r = newSession.get(target, headers=headers, auth=(api_key,'x'))
	f = open('events.txt', 'a')
	f.write(r.text)
	f.close()
	print "Event's written to: " + str(f.name)


eventIDs = fetchEvents(api_key)