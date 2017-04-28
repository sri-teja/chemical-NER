import sys
import csv
import numpy as np
from sklearn import preprocessing
import time
'''
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from  sklearn.ensemble import RandomForestClassifier
'''
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
	l1=list(reader)
#print l[0][0]
with open(sys.argv[2], 'rb') as f:
	reader=csv.reader(f,delimiter='\t')
	l2=list(reader)
train=np.array(l1)
test=np.array(l2)
#X=train[:,:-1]
le=preprocessing.LabelEncoder()
le.fit(train[:,-2])
le.classes_ = np.append(le.classes_, 'NNPS')
le.classes_ = np.append(le.classes_, 'RBR')
train[:,-2]=le.transform(train[:,-2])
test[:,-2]=le.transform(test[:,-2])
print train[:,-2]
train=train.astype(float)
test=test.astype(float)
X=train[:,:-1]
y=train[:,-1]
X_test=test[:,:-1]
y_test=test[:,-1]
print X[0]
print X_test[0]
'''
clfgnb=GaussianNB()
clfknn = KNeighborsClassifier(n_neighbors=10)
clfsvcrbf=SVC()
clfsvcpoly=SVC(kernel='poly')
clfann=MLPClassifier()
clfdt=tree.DecisionTreeClassifier()
clfrf=
'''
f=open('results_classifiers','w')
names = ["Navie Bayes","RBF SVM","Random Forest","Neural Net"]

classifiers = [GaussianNB(),SVC(gamma=2, C=1),RandomForestClassifier(max_depth=5, n_estimators=10, max_features=2,n_jobs=12),MLPClassifier()]


for name,classifier in zip(names,classifiers):
	y_pred = classifier.fit(X,y).predict(X_test)
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
	f.write("{0}\t{1}\n".format(name,':'))
	recall=tp/(tp+fn)
	f.write("{0}\t{1}\n".format('Recall:',recall))
	precision=tp/(tp+fp)
	f.write("{0}\t{1}\n".format('Precision:',precision))
	f.write("{0}\t{1}\n".format('F-score:', 2*recall*precision/(recall+precision)))
	f.write("{0}\n".format("sklearn results:"))
	tup=precision_recall_fscore_support(y_test, y_pred, average='binary')
	f.write("{0}\t{1}\t{2}\n".format(tup[0],tup[1],tup[2]))
	time.sleep(60)
