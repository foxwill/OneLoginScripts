###
# Created by: Patric Fox ( patric[dot]fox[at]onelogin[dot]com )
# Date: 02/24/2015
###
###
# requires requests, lxml, csv, and collections modules
###

import requests
import xml.etree.ElementTree as ET
import csv
from collections import defaultdict

###
# Specify the API key for your account
###
apikey = ""


###
# change user_details.csv to filename that contains list of user emails
###
columns = defaultdict(list)
with open('user_details.csv', 'rU') as f:
	reader = csv.reader(f)
	reader.next()
	for row in reader:
		for (i,v) in enumerate(row):
			columns[i].append(v)

###
# If importing from a CSV file, you must specify the column that contains the email
# address. Columns are numbered from 0 from the left.  0 , 1 , 2 , 3
###
email = columns[0]


###
# specify custom attribute that you wish to update. format should be custom_attribute_YOURATTRIBUTENAME
###
custom_attribute = 'custom_attribute_Preferred_userid'
custom_value = ''



def getUserID(email):
	###
	# function getUserID will send a request to the USER's API to determine the user's OneLogin ID Value
	# Response is received in XML and we parse the <id>VALUE</id> entry in the response and store it in the
	# userID variable
	###
	target = "https://app.onelogin.com/api/v2/users/username/" + email + "?api_key=" + apikey + "&include_custom_attributes=true"
	r = requests.get(target)
	root = ET.fromstring(r.text)
	userID = root[8].text
	return userID



def updateUser(userID):
	###
	# function updateUser expects the user's OneLogin ID as input.  When the ID is provided and the custom_attribute Value
	# is set then we make a PUT request to the API with the custom attribute in the payload and the userID in the URI.  
	# A successful post will result in a 200 OK message at which point we print a "Success" message.  If any http code other
	# than 200 is returned we output it to the command line
	###
	payload = """<user><""" + custom_attribute + """>""" + custom_value + """</""" + custom_attribute + """></user>"""
	r = requests.Session()
	r.headers['Content-Type'] = 'text/xml'
	x = r.put("https://app.onelogin.com/api/v3/users/" + userID + ".xml?api_key=" + apikey + "include_custom_attributes=true", data=payload)
	if x.status_code == 200:
		print "Success!"
	else:
		print x.status_code

###
# loop through each of the email's stored in the email variable and make a request first to getUserID and then to updateUser
###
for each in email:
	userID = getUserID(each)
	updateUser(userID)