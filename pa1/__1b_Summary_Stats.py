"""
Joshua Mausolf - CAPP 30254 HW1

This file contains the code to run the summary statistics. 
Source code for this file is documented in __1a_Stats_source_code.py and imported.

This code was written and designed to run on a MAC OSX running an Anaconda distribution of Python. Not all elements may work on Linux.

The output from running this file in terminal ($ python __1b_Summary_Stats.py) is commented
below, following the coding:
"""

from __1a_Stats_source_code import *

##_____________________________ Summary Statistics ________________________ ##


## ID
print "_"*50
print "Summary Statistics ID:"
print "Missing values: ", missing(0)
print '\n'

## First Name
print "_"*50
print "Summary Statistics First Name:"
print "Missing values: ", missing(1)
print "Mode First Name:", '\n', (data['First_name'].describe())
print '\n'

## Last Name
print "_"*50
print "Summary Statistics Last Name:"
print "Missing values: ", missing(2)
print "Mode Last Name:", '\n', (data['Last_name'].describe())
print '\n'

## State
print "_"*50
print "Summary Statistics State:"
print "Missing values: ", missing(3)
print "Mode State:", '\n', (data['State'].describe())
print '\n'

## Gender
print "_"*50
print "Summary Statistics Gender:"
print "Missing values: ", missing(4)
print "Mode Gender:", '\n', (data['Gender'].describe())
print '\n'

## Age
print "_"*50
print "Summary Statistics Age:"
print "Missing values: ", missing(5)
print "Mean Age:", '\n', (data['Age'].describe())
print "Mode Age:", '\n', (data['Age'].mode())
#Histogram
histogram('Age', 'g')

## GPA
print "_"*50
print "Summary Statistics GPA:"
print "Missing values: ", missing(6)
print "Mean GPA:", '\n', (data['GPA'].describe())
print "Mode GPA:", '\n', (data['GPA'].mode())
#Histogram
histogram('GPA', 'b')
print '\n'

## Days Missed
print "_"*50
print "Summary Statistics Days_missed:"
print "Missing values: ", missing(7)
print "Mean Days_missed:", '\n', (data['Days_missed'].describe())
print "Mode Days_missed:", '\n', (data['Days_missed'].mode())
#Histogram
histogram('Days_missed', 'r')
print '\n'

## Graduated
print "_"*50
print "Summary Statistics Graduated:"
print "Missing values: ", missing(8)
print "Mode Graduated:", '\n', (data['Graduated'].describe())
print '\n'





## ___________________ Terminal Output from Running Executing the Above Code ____________##



#joshuas-imac:Assignment_1 Joshua$ python __1b_Summary_Stats.py
#
#Total requested lines: 1000
#__________________________________________________
#Summary Statistics ID:
#Missing values:  0


#__________________________________________________
#Summary Statistics First Name:
#Missing values:  0
#Mode First Name: 
#count     1000
#unique     200
#top        Amy
#freq        12
#Name: First_name, dtype: object


#__________________________________________________
#Summary Statistics Last Name:
#Missing values:  0
#Mode Last Name: 
#count     1000
#unique     244
#top       Ross
#freq        13
#Name: Last_name, dtype: object


#__________________________________________________
#Summary Statistics State:
#Missing values:  116
#Mode State: 
#count       884
#unique       49
#top       Texas
#freq         97
#Name: State, dtype: object


#__________________________________________________
#Summary Statistics Gender:
#Missing values:  226
#Mode Gender: 
#count        774
#unique         2
#top       Female
#freq         398
#Name: Gender, dtype: object


#__________________________________________________
#Summary Statistics Age:
#Missing values:  229
#Mean Age: 
#count    771.000000
#mean      16.996109
#std        1.458067
#min       15.000000
#25%       16.000000
#50%       17.000000
#75%       18.000000
#max       19.000000
#Name: Age, dtype: float64
#Mode Age: 
#0    15
#dtype: float64


#__________________________________________________
#Summary Statistics GPA:
#Missing values:  221
#Mean GPA: 
#count    779.000000
#mean       2.988447
#std        0.818249
#min        2.000000
#25%        2.000000
#50%        3.000000
#75%        4.000000
#max        4.000000
#Name: GPA, dtype: float64
#Mode GPA: 
#0    2
#dtype: float64


#__________________________________________________
#Summary Statistics Days_missed:
#Missing values:  192
#Mean Days_missed: 
#count    808.000000
#mean      18.011139
#std        9.629371
#min        2.000000
#25%        9.000000
#50%       18.000000
#75%       27.000000
#max       34.000000
#Name: Days_missed, dtype: float64
#Mode Days_missed: 
#0     6
#1    14
#2    31
#dtype: float64


#__________________________________________________
#Summary Statistics Graduated:
#Missing values:  0
#Mode Graduated: 
#count     1000
#unique       2
#top        Yes
#freq       593
#Name: Graduated, dtype: object





