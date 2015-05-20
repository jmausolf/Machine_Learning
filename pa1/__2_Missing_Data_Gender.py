"""
Joshua Mausolf
CAPP 30254

This code was written and designed to run on a MAC OSX running an Anaconda distribution of Python. Not all elements may work on Linux.
"""

import sys
import requests
import csv
import pandas as pd 


#_____________ PART 2_______________________________________________ #

#______________Get Gender _________________#

def getGender(name):
    """Using the Genderize.io API, take a given name string and return the gender.
    """
    
    name_lower = name.lower().replace(" ", "%20")
    url = "https://api.genderize.io/?name="+name_lower
    #print url

    #Error checking
    req = requests.get(url)  
    assert req.ok, "Error: No record was found."
    data = req.json()
    assert data.get('name'), "Error: Name not found."

    # Get the Gender for a given name
    results = data['gender']
    if len(results) > 0:
        gender_id = data['gender']
        return gender_id

    elif len(results) <= 0:
        print "No gender was identified."

#Test Function
#print getGender("George")



def writeGender():
    in_file = open('mock_student_data.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_gender.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        name = row[1]
        gender = row[4]
        if gender == '':
            row[4] = getGender(name)
            writer.writerow(row)
            print getGender(name)
        else:
            row[4] = gender.lower()
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeGender()



