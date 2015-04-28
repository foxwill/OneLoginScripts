#!env/bin/python

###
# Created by: Patric Fox ( patric[dot]fox[at]onelogin[dot]com )
# Date: 02/25/2015
###
###
# requires requests, csv, and collections modules
###

import requests
import csv
from collections import defaultdict

###
# Enter API key in variable below.  use csv of user email addresses to send invites, make sure email address is in first column of csv
###

api_key = ""

columns = defaultdict(list)

###
# Specify csv of user email addresses
###

with open('userlist.csv', 'rU') as f:
	reader = csv.reader(f)
	reader.next()
	for row in reader:
		for (i,v) in enumerate(row):
			columns[i].append(v)

useremail = columns[0]



def sendInvite(useremail, api_key):
	###
	# Send invite link to user's
	###
	target = "https://app.onelogin.com/api/v3/invites/send_invite_link"
	payload = {
		"api_key":api_key,
		"email": useremail
	}
	r = requests.get(target, data=payload)
	print str(r.status_code) + " - Invitation sent to " + useremail

for each in useremail:
	sendInvite(each, api_key)
