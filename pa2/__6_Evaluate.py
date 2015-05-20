

import sys, os, re
import numpy as np
import pandas as pd
#import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
#from patsy import dmatrices
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
import pylab as pl


# Import Classifiers 
from sklearn import svm, preprocessing
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier


#Boosting and Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

#Time
import time
from threading import Timer





#______________ LOAD and DESCRIBE DATA __________________________#

#Choose Dataset
dataset = 'data/cs-training#3B.csv' #Post-impute data


def camel_to_snake(column_name):
    """
    Converts a string that is camelCase into snake_case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


#______________ CLASSIFIER FUNCTIONS ____________________________#


# ___ LOGIT ___ #

def logit_clf(dataset, DV, train):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

	model = LogisticRegression()
	
	if train=='yes':
		model1 = model.fit(X_train, y_train)
		print "Classifier: Logistic Regression"
		print pd.DataFrame(zip(X.columns, np.transpose(model.coef_)))
		end = time.time()
		print "Runtime, base model: %.3f" % (end-start), "seconds."
		return model1
	elif train=='no':
		model2 = model.fit(X, y)
		print "Classifier: Logistic Regression"
		print pd.DataFrame(zip(X.columns, np.transpose(model.coef_)))
		end = time.time()
		print "Runtime, base model: %.3f" % (end-start), "seconds."
		return model2



#print logit_clf('data/cs-training#3B.csv', 'serious_dlqin2yrs')


# ___ LINEAR SVM ___ #

def Build_Data_Set(dataset, DV, lower_limit=0, upper_limit=''):
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	X = preprocessing.scale(X)

	return X[lower_limit:upper_limit],y[lower_limit:upper_limit]

def lin_svc(dataset, DV, lower_limit=0, upper_limit=''):
	"""Runs a linear for a given DV, using all remaining
	variables as features.
	Prohibitive run time for N > 20,000. Cross-validation even worse.
	Consider anova_svm instead.""" 



	start = time.time()

	X, y = Build_Data_Set(dataset, DV, lower_limit, upper_limit)

	clf = SVC(kernel="linear", C= 1.0)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Linear SVC"
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 


#lin_svc('data/cs-training#3B.csv', 'serious_dlqin2yrs', 0, 150000)

def anova_svm(dataset, DV, k, lower_limit=0, upper_limit=''):
	start = time.time()

	X, y = Build_Data_Set(dataset, DV, lower_limit, upper_limit)

	# ANOVA SVM-C
	# 1) anova filter, take 3 best ranked features
	anova_filter = SelectKBest(f_regression, k=3)
	# 2) svm
	clf = SVC(kernel='linear', probability=True, C=0.5, cache_size=10000)

	anova_svm = make_pipeline(anova_filter, clf)
	model = anova_svm.fit(X, y)

	end = time.time()
	print "Classifier: Anova Linear SVM, "+str(k)+"-best features"
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 

#print anova_svm('data/cs-training#3B.csv', 'serious_dlqin2yrs', 3, 0, 20000)


# ___ DECISION TREE ___ #

def d_tree(dataset, DV, max_dep):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]


	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]


	clf = tree.DecisionTreeClassifier(max_depth=max_dep)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Decision Tree,", "Depth = ", max_dep
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 

#d_tree('data/cs-training#3B.csv', 'serious_dlqin2yrs', 5)


# ___ RANDOM FOREST ___ #

def random_forest(dataset, DV, max_dep):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	clf = RandomForestClassifier(n_jobs=2, max_depth=max_dep)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Random Forest,", "Depth = ", max_dep
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 

#random_forest('data/cs-training#3B.csv', 'serious_dlqin2yrs', 5)


# ___ BAGGING ___ #

def random_forest_bagging(dataset, DV, max_dep):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	clf = BaggingClassifier(RandomForestClassifier(n_jobs=2, max_depth=max_dep), max_samples=0.5, max_features=0.5)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Random Forest with Bagging,", "Depth = ", max_dep
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 


#random_forest_bagging('data/cs-training#3B.csv', 'serious_dlqin2yrs', 5)


# ___ BOOSTING ___ #

def random_forest_boosting(dataset, DV, max_dep):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	clf = AdaBoostClassifier(RandomForestClassifier(n_jobs=2, max_depth=max_dep), n_estimators=20)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Random Forest with Boosting,", "Depth = ", max_dep
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 

#random_forest_boosting('data/cs-training#3B.csv', 'serious_dlqin2yrs', 2)



def gradient_boosting(dataset, DV, max_dep):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=max_dep, random_state=0)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: Gradient Boosting,", "Depth = ", max_dep
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 


#gradient_boosting('data/cs-training#3B.csv', 'serious_dlqin2yrs', 3)


# ___ KNN ___ #

def KNN(dataset, DV, neighbors, method='auto'):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]


	#DV
	y = data[str(DV)]
	X = data[data.columns - [str(DV)]]

	clf = KNeighborsClassifier(n_neighbors=neighbors, algorithm=method, leaf_size=5)
	model = clf.fit(X, y)

	end = time.time()
	print "Classifier: KNN,", "neighbors = ", neighbors, ", algorithm = ", method
	print "Runtime, base model: %.3f" % (end-start), "seconds."
	return model 

KNN('data/cs-training#3B.csv', 'serious_dlqin2yrs', 3, 'kd_tree')


#______________ PRECISION RECALL CURVE ____________________________#

def plot_precision_recall_curve(y_test, y_score, model):
	# Compute Precision-Recall and plot curve
	precision, recall, thresholds = precision_recall_curve(y_test, y_score[:, 1])
	area = auc(recall, precision)
	print "Area Under Curve: %0.2f" % area

	pl.clf()
	pl.plot(recall, precision, label='Precision-Recall curve')
	pl.xlabel('Recall')
	pl.ylabel('Precision')
	pl.ylim([0.0, 1.05])
	pl.xlim([0.0, 1.0])
	pl.title('Precision-Recall example: AUC=%0.2f' % area)
	pl.legend(loc="lower left")

	plt.draw()
	plt.savefig("output/evaluation/"+model+"_precision-recall-curve"+".jpg")
	plt.clf()



#______________ EVALUATION FUNCTIONS ____________________________#



def evalualte_base(dataset, DV, model):
	start = time.time()
	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	if model == 'logit':
		#DV
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]

		clf = logit_clf(dataset, DV, 'yes')


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

	# predict class labels for the test set
	predicted = clf.predict(X_test)

	#print predicted

	# generate class probabilities
	y_score = clf.predict_proba(X_test)
	
	# generate evaluation metrics
	print "Model score, accuracy : %.3f" % (metrics.accuracy_score(y_test, predicted))
	print "Model score, roc_auc: %.3f" % (metrics.roc_auc_score(y_test, y_score[:, 1]))
	print "Model score, f1: %.3f" % metrics.f1_score(y_test, predicted)
	print "Model score, average-precision: %.3f" % (metrics.average_precision_score(y_test, predicted))
	print "Model score, precision: %.3f" % (metrics.precision_score(y_test, predicted))
	print "Model score, recall: %.3f" % (metrics.recall_score(y_test, predicted))

	end = time.time()
	print "Runtime, K-folds evaluation of base model: %.3f" % (end-start), "seconds."

#evalualte_base('data/cs-training#3B.csv', 'serious_dlqin2yrs', 'logit')



def evalualte_K_fold(dataset, DV, model, sets):
	start = time.time()

	# Load Data to Pandas
	data = pd.read_csv(dataset, index_col=0)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#Metrics
	metrics = ['accuracy', 'average_precision', 'precision', 'recall', 'f1', 'roc_auc', 'log_loss', 'mean_squared_error', 'r2']
	

	if model == 'logit':
		#DV
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = logit_clf(dataset, DV, 'no')


	elif model == 'lin_svc':
		X, y = Build_Data_Set(dataset, DV, 0, 150000)
		clf = lin_svc(dataset, DV, 0, 150000)


	elif model == 'anova_svm':
		X, y = Build_Data_Set(dataset, DV, 0, 150000)
		clf = anova_svm(dataset, DV, 3, 0, 150000)

	elif model == 'd_tree':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = d_tree(dataset, DV, 4)

	elif model == 'random_forest':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = random_forest(dataset, DV, 5)
		#clf = random_forest(dataset, DV, 10)

	elif model == 'random_forest_bagging':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = random_forest_bagging(dataset, DV, 5)

	elif model == 'random_forest_boosting':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = random_forest_boosting(dataset, DV, 5)

	elif model == 'gradient_boosting':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		clf = gradient_boosting(dataset, DV, 3)


	elif model == 'KNN':
		y = data[str(DV)]
		X = data[data.columns - [str(DV)]]
		#clf = KNN(dataset, DV, 3)
		clf = KNN(dataset, DV, 3)

	
	if sets==1:


		print "Model score: ", clf.score(X, y)
		print "Baseline = Mean of DV: ", y.mean()
		print "Prediction - null: ", clf.score(X, y) - (1-y.mean())



	if sets >1:
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
		
		# evaluate the model using N-fold cross-validation
		try:
			y_score = clf.fit(X_train, y_train).predict_proba(X_test)
			plot_precision_recall_curve(y_test, y_score, model)
		except:
			pass
		print "Cross-validation of "+model+" classifier: "+str(sets)+"-folds"
		print "Baseline = 1-Mean of DV: %.3f" % (1-y.mean())
		for metric in metrics:
			scores = cross_val_score(clf, X, y, scoring=str(metric), cv=sets)
			print "Model mean score, "+metric+" : %.3f" % (scores.mean())
		end = time.time()
		print "Runtime, K-folds evaluation of base model: %.3f" % (end-start), "seconds."



#______________ GENERATE EVALUATIONS ____________________________#



#classifiers = ['logit', 'anova_svm', 'd_tree', 'random_forest', 'random_forest_bagging', 'random_forest_boosting', 'gradient_boosting', 'KNN']
classifiers = ['KNN']


# Five-Fold Cross Validation
def EVAL():

	for clf in classifiers:
		print "__"*50, "\n"
		evalualte_K_fold('data/cs-training#3B.csv', 'serious_dlqin2yrs', clf, 5)
		print "__"*50, "\n"

EVAL()