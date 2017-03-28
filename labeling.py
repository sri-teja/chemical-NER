import csv
import sys
import nltk
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

f = open('input/chemical_list.csv', 'rb')
reader = csv.reader(f)
chemical_entities = []
ans_word_lemmas = []
ans_word_n_grams = []
for row in reader:
	i = row[4].decode("utf8")
	words = word_tokenize(i)
	ans_lemmas = []
	for j in words:
		ans_lemmas.append(wordnet_lemmatizer.lemmatize(j))
	ans_word_n_grams.append(''.join(ans_lemmas))
#print ans_word_n_grams
print "******* finished creating labels *************\n"
