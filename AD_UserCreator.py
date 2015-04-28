###
# Created by: Patric Fox ( patric[dot]fox[at]onelogin[dot]com )
# Date: 02/25/2015
###
###
# requires requests, csv, and collections modules
###

import random
import os

###
# Lets create some fake names.  We need to make sure we have
# Name, samAccountName, Description, Department, EmployeeID, Path, and Enabled
###

###
# Values to generate random names
# Be sure to update the Departments (OU's), Path (DN's of OU's) and the dc info
###

fname = ["Nancy","Fancy","Joan","Bob","Tom","Joe","Larry","Frank"]
lname = ["McCoy","HatField","Smith","Skywalker","Jones","Adams","McClusky","Benders"]
samCount = 0
department = ["Testing","Testing Oscar","Testing OneLogin","Users"]
employeeID = 10
path = ["OU=Testing","OU=Testing Oscar","OU=Testing OneLogin","OU=Users"]
dc = ",DC=OLtesting,DC=com"
enabled = "True"
output = []



###
# Set range value to number of user's you wish to create
###

for x in range(5):
	first = random.choice(fname)
	last = random.choice(lname)
	name = first + " " + last
	samName = str.lower(first+last+str(samCount))
	samCount += 1
	depa = random.choice(department)
	emp = str(employeeID)
	employeeID += 10
	pth = random.choice(path)
	record = 'dsadd user CN="' + samName + str(samCount) + ',' + pth + dc + '" -upn ' + samName+ '@oltesting.com' +' -empid '\
	+ str(employeeID) +' -pwd P@ssw0rd2@ -fn ' + first + ' -ln ' + last + ' -display ' +\
	'"' + name + '"' + ' -email ' + samName+str(samCount) + '@oltesting.com' + \
	' -pwdneverexpires yes -disabled no -acctexpires never'

	###
	#check for the record that was just created in the output list, if record exists, create another one, if not, write
	# the output to the list for recording
	###

	if record not in output:
		output.append(record)

###
# Lets remove any existing files so we do not write the same user record twice"""
###

try:
	os.remove('output.txt')
except:
	pass

###
# Write the output to output.txt
###

f = open('output.txt', 'w')
for each in output:
	f.write(each + "\n")

f.close()
