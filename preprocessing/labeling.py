import csv
import sys
import nltk
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#gold_train_file = "../data/cemp_training_set/chemdner_cemp_gold_standard_train.tsv"
gold_train_file = "./chemical_list.csv"
f = open(gold_train_file, 'rb')
#reader = csv.reader(f,delimiter='\t')
reader = f.readlines()
chemical_entities = []
ans_word_lemmas = []
ans_word_n_grams = []
for row in reader:
	#print row
	#i = row[4].decode("utf8")
	rl=row.split(",")
	i=rl[4]
	if len(rl)!=7:
		i=','.join(rl[4:-1])
	#words = word_tokenize(i)
	words = (i.strip()).split(" ")
	ans_lemmas = []
	#for j in words:
	#	ans_lemmas.append(wordnet_lemmatizer.lemmatize(j))
	#ans_word_n_grams.append(''.join(ans_lemmas))
	ans_word_n_grams.append(''.join(words))
#print ans_word_n_grams
print "******* finished creating labels *************\n"
