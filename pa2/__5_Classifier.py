"""
Joshua Mausolf - CAPP 30254 Assignment 2

In this python module I develop several functions, chiefly a logistic regression classifier,
and a second function to help export the regression results.

I have unhashed several of the functions so that the module may be run from terminal.
Other examples are left hashed.
"""

import sys, os, re
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

# Import Classifiers 
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model


#______________ LOAD and DESCRIBE DATA __________________________#

#Choose Dataset
dataset = 'data/cs-training#3B.csv' #Post-impute data


#______________ CLASSIFIER FUNCTIONS ____________________________#

def camel_to_snake(column_name):
    """
    Converts a string that is camelCase into snake_case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def logistic_regression_classifier2(dataset, DV, train='no'):
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

	model = LogisticRegression()

	if train=='yes':
		model.fit(X_train, y_train)
		return model, X, y, X_train, X_test, y_train, y_test
	else:
		model = model.fit(X, y)
		return model, X, y




#clf_log = logistic_regression_classifier2(dataset, 'serious_dlqin2yrs')
#print clf_log

def logistic_regression_classifier(dataset, DV, sets=1):
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]


	# Assume no test/train split
	if sets==1:
		model1 = LogisticRegression()
		model1 = model1.fit(X, y)
		#Print coefficients
		print pd.DataFrame(zip(X.columns, np.transpose(model1.coef_)))

		# check the accuracy
		print "Model score:", '\n', model1.score(X, y)
		print "Prediction - null: ", model1.score(X, y) - (1-y.mean())


	elif sets==2:
		# evaluate the model by splitting into train and test sets
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
		model2 = LogisticRegression()
		model2.fit(X_train, y_train)

		#Print coefficients
		#print pd.DataFrame(zip(X.columns, np.transpose(model2.coef_)))

		#Score2 = model2.score(X_train, y_train)
		#print "Model score:", '\n', Score2
		#print "Prediction - null: ", Score2 - (1-y.mean())



		# predict class labels for the test set
		predicted = model2.predict(X_test)

		#print predicted

		# generate class probabilities
		y_score = model2.predict_proba(X_test)
		#print probs

		# generate evaluation metrics
		print "metrics, accuracy", metrics.accuracy_score(y_test, predicted)
		print "metrics, roc_auc", metrics.roc_auc_score(y_test, y_score[:, 1])
		print metrics.f1_score(y_test, predicted)
		print metrics.average_precision_score(y_test, predicted)
		print metrics.precision_score(y_test, predicted)
		print metrics.recall_score(y_test, predicted)


	elif sets >2:
		# evaluate the model by splitting into train and test sets
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
		model3 = LogisticRegression()
		model3.fit(X_train, y_train)

		#Print coefficients
		print pd.DataFrame(zip(X.columns, np.transpose(model3.coef_)))

		# evaluate the model using N-fold cross-validation
		folds=sets 
		scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=folds)
		print "Model mean score:", '\n', scores.mean()
		print "Prediction mean - null: ", scores.mean()-(1-y.mean())
		print model3.predict_proba(X)


# Unhash to test:
#logistic_regression_classifier('cs-training#3B.csv', 'serious_dlqin2yrs', 1)
logistic_regression_classifier('data/cs-training#3B.csv', 'serious_dlqin2yrs', 2)
#logistic_regression_classifier(dataset, 'serious_dlqin2yrs', 10)



def logistic_regression_table(dataset, DV, table='no', CSV='no'):
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	logit = sm.Logit(y, X)
	model = logit.fit()

	#Prediction
	prediction = 'prediction_'+str(DV)
	data[prediction] = model.predict(X)

	#Redidual
	data['residual_'+str(DV)] = data[str(DV)] - data[prediction]
	#print data.head()

	if table == 'table':
		model_output = model.summary()
		odds_ratio = '\n'+"Odd's Ratios:"+'\n'+str(np.exp(model.params))+'\n'
		f = open("output/logistic_regression_table.txt", 'w')
		f.write(str(model_output))
		f.write(str(odds_ratio))
		f.close

		#Write CSV Option
		if CSV == 'csv':
			data.to_csv('data/logit_data_prediction_residuals.csv', encoding='utf-8')
		else:
			pass


	else:
		print model.summary()
		print "Odd's Ratios:", '\n', np.exp(model.params), '\n'

	
		#Write CSV Option
		if CSV == 'csv':
			data.to_csv('data/logit_data_prediction_residuals.csv', encoding='utf-8')
		else:
			pass


# Unhash to test:
#logistic_regression_table(dataset, 'serious_dlqin2yrs')
#logistic_regression_table(dataset, 'serious_dlqin2yrs', 'table')
#logistic_regression_table(dataset, 'serious_dlqin2yrs', 'no-table', 'csv')
#logistic_regression_table(dataset, 'serious_dlqin2yrs', 'table', 'csv')

