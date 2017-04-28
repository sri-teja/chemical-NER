import numpy as np
from sklearn.model_selection import train_test_split
import sys
import csv
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import precision_recall_fscore_support

with open(sys.argv[1], 'rb') as f:
	reader=csv.reader(f,delimiter='\t')
	l=list(reader)
train=np.array(l)
le=preprocessing.LabelEncoder()
le.fit(train[:,-2])
train[:,-2]=le.transform(train[:,-2])
print train[:,-2]
train=train.astype(float)
data=train[:,:-1]
target=train[:,-1]
print target
X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3, random_state=0)
f=open('results_classifiers.txt','w')
names = ["Navie Bayes","RBF SVM","Random Forest","Neural Net"]

classifiers = [GaussianNB(),SVC(gamma=2, C=1),RandomForestClassifier(max_depth=10, n_estimators=10, max_features=5,n_jobs=12),MLPClassifier()]


for name,classifier in zip(names,classifiers):
	y_pred = classifier.fit(X_train,y_train).predict(X_test)
	tp=0.0
	fn=0.0
	tn=0.0
	fp=0.0
	for i,j in zip(y_test,y_pred):
		if i==1:
			if j==1:
				tp+=1
			else:
				fn+=1
		else:
			if j==1:
				fp+=1
			else:
				tn+=1
#	f.write("{0}\t{1}\n".format(name,':'))
	recall=tp/(tp+fn)
#	f.write("{0}\t{1}\n".format('Recall:',recall))
	precision=tp/(tp+fp)
#	f.write("{0}\t{1}\n".format('Precision:',precision))
#	f.write("{0}\t{1}\n".format('F-score:', 2*recall*precision/(recall+precision)))
	f.write("{0}\n".format("sklearn results:"))
	tup=precision_recall_fscore_support(y_test, y_pred)
	#f.write("{0}\t{1}\t{2}\n".format('Precision','Recall','F-Score'))
	print 'Precision','Recall','F-Score'
	#f.write("{0}\t{1}\t{2}\n".format(tup[0],tup[1],tup[2]))
	print tup[0],tup[1],tup[2]
	print tup
'''clf = GaussianNB()
clf.fit(X_train, y_train)
#print clf.score(X_test, y_test)
y_pred = clf.predict(X_test)
tp=0.0
fn=0.0
tn=0.0
fp=0.0
for i,j in zip(y_test,y_pred):
	if i==1:
		if j==1:
			tp+=1
		else:
			fn+=1
	else:
		if j==1:
			fp+=1
		else:
			tn+=1
print tp,fp,fn,tn
recall=tp/(tp+fn)
print 'Recall:',recall
precision=tp/(tp+fp)
print 'Precision:',precision
print 'F-score:', 2*recall*precision/(recall+precision)
#tup=precision_recall_fscore_support(y_test, y_pred, average='binary')'''
