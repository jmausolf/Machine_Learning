"""
Joshua Mausolf - CAPP 30254 HW1

This file contains the source code to run the summary statistics. 
Source code for this file is executed in __1b_Summary_Stats.py. The summary stats output is
commented in that file, following the coding.

This code was written and designed to run on a MAC OSX running an Anaconda distribution of Python. Not all elements may work on Linux.
"""

import csv
import pandas as pd 
import matplotlib.pyplot as plt
import subprocess

def read_CSV(i):
	"""Reads the CSV of Mock Student Data for a Given Line i"""
	with open('mock_student_data.csv', 'rU') as data_file:
		reader = csv.reader(data_file)
		lines = list(reader)
		output = lines[i]
		return output


#Draw Histogram Function
def histogram(variable, color):
	fig = data[variable].hist(color=color)
	fig.set_xlabel(variable) #defines the x axis label
	fig.set_ylabel('Number of Respondents') #defines y axis label
	fig.set_title(variable+' Distribution') #defines graph title
	plt.draw()
	plt.savefig(variable+"_histogram.jpg")
	command = "open "+variable+"_histogram.jpg"
	subprocess.call(command, shell=True)
	plt.clf()


with open('mock_student_data.csv', 'rU') as data_file:
	reader = csv.reader(data_file)
	lines = list(reader)
	XR = len(lines)
	print "Total requested lines:", XR-1


def missing(column):
	missing = 0
	for line in range(1, XR):
		req_line = read_CSV(line)
		if req_line[column] == '':
			missing += 1
	return missing



#Read CSV Data into Panda's Data Frame
data = pd.read_csv('mock_student_data.csv')









