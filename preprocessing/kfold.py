import os
import sys
import subprocess
from os import listdir
from os.path import isfile, join

recall = []
precision = []
fscore = []

for j in range(0,10):
	os.system("python testfile.py "+sys.argv[1])
	#subprocess.call(["crf_learn", "./template/template.txt", "./features/trainfeatures.txt", "./features/train_model"])
	os.system("crf_learn -p 12 -c 3.0 ../template/template.txt ../data/train_features.txt ../data/train_model_fin")
	#subprocess.call(["crf_test", "-m", "./features/train_model", "./features/"+files_in_features[j], ">", "./output/"+files_in_features[j]+"_output.txt"])
	os.system("crf_test -m ../data/train_model_cemp ../data/test_features.txt"+" > final_output.txt")
	
	## accuracy 
	contents_file = open("cemp_output.txt").read()
	tp = float(contents_file.count("1\t1\n"))
	fp = float(contents_file.count("0\t1\n"))
	tn = float(contents_file.count("0\t0\n"))
	fn = float(contents_file.count("1\t0\n"))
	
	try:
		recall.append(tp/(tp+fn)*100)
		precision.append(tp/(tp+fp)*100)
		fscore.append(((2 * recall[j] * precision[j])/(recall[j]+precision[j])))
	except:
		recall.append(0)
		precision.append(0)
		fscore.append(0)
	print "iteration:",j
	print "Recall = ", recall[j]
	print "Precision = ", precision[j]
	print "F-score = ", fscore[j]

print "Avg. Recall = ", sum(recall)/len(recall)
print "Avg. precision = ", sum(precision)/len(precision)
print "Avg. F-Score = ", sum(fscore)/len(fscore)
print "Program done."

