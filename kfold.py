import os
import subprocess

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./input/text/') if isfile(join('./input/text/', f))]

print onlyfiles
recall = []
precision = []
fscore = []
os.system("rm -r ./features/*")

for i in onlyfiles:
	print "Running " ,i
	#subprocess.call(["python features.py" , "./input/text/"+i, "./features/"+ i.split(".")[0] + "_trainfeatures.txt"], shell=True)
	os.system("python features.py ./input/text/"+i+" ./features/"+ i.split(".")[0]+"_trainfeatures.txt")


files_in_features = [f for f in listdir('./features') if isfile(join('./features', f))]

for j in range(len(files_in_features)):
	with open("./features/trainfeatures.txt", "wb") as outfile:
		for i in files_in_features[:j] + files_in_features[j+1:]:
			with open("./features/"+i, "rb") as infile:
				outfile.write(infile.read())
	print "-------------"
	#subprocess.call(["crf_learn", "./template/template.txt", "./features/trainfeatures.txt", "./features/train_model"])
	os.system("crf_learn ./template/template.txt ./features/trainfeatures.txt ./features/train_model")
	#subprocess.call(["crf_test", "-m", "./features/train_model", "./features/"+files_in_features[j], ">", "./output/"+files_in_features[j]+"_output.txt"])
	os.system("crf_test -m ./features/train_model ./features/"+files_in_features[j]+" > ./output/"+onlyfiles[j].split(".")[0]+"_output.txt")
	
	## accuracy 
	contents_file = open("./output/"+onlyfiles[j].split(".")[0]+"_output.txt").read()
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
	print onlyfiles[j], ":"
	print "Recall = ", recall[j]
	print "Precision = ", precision[j]
	print "F-score = ", fscore[j]
	os.remove("./features/trainfeatures.txt")
	os.remove("./features/train_model")

print "Avg. Recall = ", sum(recall)/len(recall)
print "Avg. precision = ", sum(precision)/len(precision)
print "Avg. Recall = ", sum(fscore)/len(fscore)
print "Program done."


	
	
	

