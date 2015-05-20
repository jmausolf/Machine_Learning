"""
Joshua Mausolf
CAPP 30254

This code was written and designed to run on a MAC OSX running an Anaconda distribution of Python. Not all elements may work on Linux.
"""

import sys
import csv
import pandas as pd 


#_____________ PART 3A _______________________________________________ #

#______________Get Means_________________#

## I made the choice to round to the nearest integer values to match the formatting for the existing database. Terminal results of the means are text commented after the code below:

#Read CSV Data into Panda's Data Frame
data = pd.read_csv('mock_student_data.csv')

#Mean Age
m_Age = data['Age'].mean()
meanAge = int(round(m_Age))
#print m_Age
#print meanAge

#Mean GPA
m_GPA = data['GPA'].mean()
meanGPA = int(round(m_GPA))
#print m_GPA
#print meanGPA

#Mean Day's Missed
m_Days_missed = data['Days_missed'].mean()
meanDays_missed = int(round(m_Days_missed))
#print m_Days_missed
#print meanDays_missed

## Age 
#16.9961089494
#17

## GPA
#2.98844672657
#3

## Days_missed
#18.0111386139
#18

#______________Write Results_________________#

def writeAge_mean():
    in_file = open('mock_student_data_gender.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_age#3A.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        age = row[5]
        if age == '':
            row[5] = meanAge
            writer.writerow(row)
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeAge_mean()

def writeGPA_mean():
    in_file = open('mock_student_data_age#3A.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_GPA#3A.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        gpa = row[6]
        if gpa == '':
            row[6] = meanGPA
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeGPA_mean()

def writeDays_missed_mean():
    in_file = open('mock_student_data_GPA#3A.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_Days_missed#3A.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        days_missed = row[7]
        if days_missed == '':
            row[7] = meanDays_missed
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeDays_missed_mean()



#_____________ PART 3B _______________________________________________ #

#______________Get Class Conditional Means_________________#

## I made the choice to round to the nearest integer values to match the formatting for the existing database. Terminal results of the class conditional means are text commented after the code below:


#Read CSV Data into Panda's Data Frame
data = pd.read_csv('mock_student_data.csv')
graduated = data.groupby('Graduated')


#Mean Age
cm_Age = graduated['Age'].mean()
cmeanAge_no_grad = int(round(cm_Age[0])) # No (Graduated)
cmeanAge_yes_grad = int(round(cm_Age[1])) # Yes (Graduated)
#print cm_Age
#print cmeanAge_no_grad, cmeanAge_yes_grad


#Mean GPA
cm_GPA = graduated['GPA'].mean()
cmeanGPA_no_grad = int(round(cm_GPA[0])) # No (Graduated)
cmeanGPA_yes_grad = int(round(cm_GPA[1])) # Yes (Graduated)
#print cm_GPA
#print cmeanGPA_no_grad, cmeanGPA_yes_grad

#Mean Day's Missed
cm_Days_missed = graduated['Days_missed'].mean()
cmeanDays_missed_no_grad = int(round(cm_Days_missed[0])) # No (Graduated)
cmeanDays_missed_yes_grad = int(round(cm_Days_missed[1])) # Yes (Graduated)
#print cm_Days_missed
#print cmeanDays_missed_no_grad, cmeanDays_missed_yes_grad

#Results from printed output in terminal:


## Age 
#Graduated
#No           17.051780
#Yes          16.958874
#Name: Age, dtype: float64
#17 17

## GPA
#Graduated
#No           2.515971
#Yes          3.505376
#Name: GPA, dtype: float64
#3 4

## Days_missed
#Graduated
#No           19.228501
#Yes          16.775561
#Name: Days_missed, dtype: float64
#19 17


#______________Write Results_________________#

def writeAge_cmean():
    in_file = open('mock_student_data_gender.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_age#3B.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        age = row[5]
        graduated = row[8]
        if age == '':
            if graduated == 'No':
                row[5] = cmeanAge_no_grad
                writer.writerow(row)
            elif graduated == 'Yes':
                row[5] = cmeanAge_yes_grad
                writer.writerow(row)
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeAge_cmean()

def writeGPA_cmean():
    in_file = open('mock_student_data_age#3B.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_GPA#3B.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        gpa = row[6]
        graduated = row[8]
        if gpa == '':
            if graduated == 'No':
                row[6] = cmeanGPA_no_grad
                writer.writerow(row)
            elif graduated == 'Yes':
                row[6] = cmeanGPA_yes_grad
                writer.writerow(row)
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeGPA_cmean()

def writeDays_missed_cmean():
    in_file = open('mock_student_data_GPA#3B.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_Days_missed#3B.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        days_missed = row[7]
        graduated = row[8]
        if days_missed == '':
            if graduated == 'No':
                row[7] = cmeanDays_missed_no_grad
                writer.writerow(row)
            elif graduated == 'Yes':
                row[7] = cmeanDays_missed_yes_grad
                writer.writerow(row)
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeDays_missed_cmean()



#_____________ PART 3C _______________________________________________ #

#______________Get Alternate Means_________________#

### ******* Explanation 
"""
Part 3C: One possible method that might be better than the simple bivariate class-conditional mean used in 3B, would be to use a class-conditional mean that not only conditions on whether an individual graduated, but also conditions on GENDER. Theoretically, there are adundant empiricle studies noting gender disparities in education. I argue that paying deference to this fact makes sense in this case when predicting missing values. I have done this below.

    * I note, that I have a sense that there are some more advanced forms of imputation using regression or covariance predictors, but do not currently have the statistical knowledge to know when and how to deploy these alternate methods.  
"""
### ******* 

## I made the choice to round to the nearest integer values to match the formatting for the existing database. Terminal results of the alternate class conditional means are text commented after the code below:


#Read CSV Data into Panda's Data Frame
data = pd.read_csv('mock_student_data.csv')
graduated_gender = data.groupby(['Graduated', 'Gender'])


#Mean Age
am_Age = graduated_gender['Age'].mean()
ameanAge_no_grad_fem = int(round(am_Age[0])) # No (Graduated) - female
ameanAge_no_grad_male = int(round(am_Age[1])) # No (Graduated) - male
ameanAge_yes_grad_fem = int(round(am_Age[2])) # Yes (Graduated) - female
ameanAge_yes_grad_male = int(round(am_Age[3])) # Yes (Graduated) - male
#print am_Age
#print ameanAge_no_grad_fem, ameanAge_no_grad_male, ameanAge_yes_grad_fem,ameanAge_yes_grad_male


#Mean GPA
am_GPA = graduated_gender['GPA'].mean()
ameanGPA_no_grad_fem = int(round(am_GPA[0])) # No (Graduated) - female
ameanGPA_no_grad_male = int(round(am_GPA[1])) # No (Graduated) - male
ameanGPA_yes_grad_fem = int(round(am_GPA[2])) # Yes (Graduated) - female
ameanGPA_yes_grad_male = int(round(am_GPA[3])) # Yes (Graduated) - male
#print am_GPA
#print ameanGPA_no_grad_fem, ameanGPA_no_grad_male, ameanGPA_yes_grad_fem, ameanGPA_yes_grad_male

#Mean Day's Missed
am_Days_missed = graduated_gender['Days_missed'].mean()
ameanDays_missed_no_grad_fem = int(round(am_Days_missed[0])) # No (Graduated) - female
ameanDays_missed_no_grad_male = int(round(am_Days_missed[1])) # No (Graduated) - male
ameanDays_missed_yes_grad_fem = int(round(am_Days_missed[2])) # Yes (Graduated) - female
ameanDays_missed_yes_grad_male = int(round(am_Days_missed[3])) # Yes (Graduated) - male
#print am_Days_missed
#print ameanDays_missed_no_grad_fem, ameanDays_missed_no_grad_male, ameanDays_missed_yes_grad_fem, ameanDays_missed_yes_grad_male

#Results from printed output in terminal:

## Age 
#Graduated  Gender
#No         Female    17.008850
#           Male      17.218487
#Yes        Female    16.859375
#           Male      16.969880
#Name: Age, dtype: float64
#17 17 17 17

## GPA
#Graduated  Gender
#No         Female    2.496774
#           Male      2.547771
#Yes        Female    3.510067
#           Male      3.496454
#Name: GPA, dtype: float64
#2 3 4 3

## Days_missed
#Graduated  Gender
#No         Female    19.129032
#           Male      19.248408
#Yes        Female    17.185185
#           Male      15.268966
#Name: Days_missed, dtype: float64
#19 19 17 15


#______________Write Results_________________#

def writeAge_amean():
    in_file = open('mock_student_data_gender.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_age#3C.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        age = row[5]
        gender = row[4]
        graduated = row[8]
        if age == '':
            if graduated == 'No':
                if gender == 'female':
                    row[5] = ameanAge_no_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[5] = ameanAge_no_grad_male
                    writer.writerow(row)          
            elif graduated == 'Yes':
                if gender == 'female':
                    row[5] = ameanAge_yes_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[5] = ameanAge_yes_grad_male
                    writer.writerow(row) 
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeAge_amean()

def writeGPA_amean():
    in_file = open('mock_student_data_age#3C.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_GPA#3C.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        gpa = row[6]
        gender = row[4]
        graduated = row[8]
        if gpa == '':
            if graduated == 'No':
                if gender == 'female':
                    row[6] = ameanGPA_no_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[6] = ameanGPA_no_grad_male
                    writer.writerow(row)          
            elif graduated == 'Yes':
                if gender == 'female':
                    row[6] = ameanGPA_yes_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[6] = ameanGPA_yes_grad_male
                    writer.writerow(row) 
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeGPA_amean()

def writeDays_missed_amean():
    in_file = open('mock_student_data_GPA#3C.csv', 'rU')
    reader = csv.reader(in_file)
    out_file = open('mock_student_data_Days_missed#3C.csv', "wb")
    writer = csv.writer(out_file)
    for row in reader:
        days_missed = row[7]
        gender = row[4]
        graduated = row[8]
        if days_missed == '':
            if graduated == 'No':
                if gender == 'female':
                    row[7] = ameanDays_missed_no_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[7] = ameanDays_missed_no_grad_male
                    writer.writerow(row)          
            elif graduated == 'Yes':
                if gender == 'female':
                    row[7] = ameanDays_missed_yes_grad_fem
                    writer.writerow(row)
                elif gender == 'male':
                    row[7] = ameanDays_missed_yes_grad_male
                    writer.writerow(row) 
        else:
            writer.writerow(row)
    in_file.close()
    out_file.close()

#Unhash to run
writeDays_missed_amean()
