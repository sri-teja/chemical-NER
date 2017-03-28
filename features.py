import nltk
import sys
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from pre_processing import *

#given_word = sys.argv[1]
#word_lemma = wordnet_lemmatizer.lemmatize(given_word)
#word_tag = nltk.pos_tag(given_word)


exclude = set(string.punctuation)
#print exclude

print "*********** Creating the features for each word **********"
def get_features(str1):
	u = 0
	l = 0
	c = 0
	pun = 0
	char_count = 0
	case_pattern = ""
	allow = 0
	n_gram = ""
	# for generating the n-grams of a token of length less than 4 from start and end
	if len(str1)>3:
		valid = 1
		n_gram = list("12345678")
		n_gram[0] = str1[0]
		n_gram[1] = str1[0:1]
		n_gram[2] = str1[0:2]
		n_gram[3] = str1[0:3]
		n_gram[4] = str1[-1:]
		n_gram[5] = str1[-2:]
		n_gram[6] = str1[-3:]
		n_gram[7] = str1[-4:]
		n_gram = "".join(n_gram)
	else:
		valid = 0
	for i in str1:
		char_count +=1
		if char_count <= 8: # for case_pattern of first 8 letters in a token
			allow = 1
		
		if i.isupper(): # for uppercase letters in a token
			u +=1
			if allow == 1:
				case_pattern += 'A' # add 'A' to case_pattern 
		
		if i.islower():
			l +=1
			if allow ==1:
				case_pattern += 'a' # add 'a' to case_pattern
		
		if i.isdigit():
			c += 1
			if allow ==1:
				case_pattern += '0' # add '0' to case_pattern
		
		if i in exclude and pun==0:
		 	pun = 1
			
	return u, l, c, pun, case_pattern, valid, n_gram

features = []
for i in word_n_grams:
	
	#uppercase_count, lowercase_count, digit_count, has_punctuation, case_pattern, validity, n_gram = get_features(i)
	features.append(get_features(i))
#print uppercase_count
#print features
		

extract_file_name = str(''.join((sys.argv[1]).split('/')[0:-1])) + '/' + str(sys.argv[1]).split('/')[-1:][0].split('.')[0]+"_features.txt"
f= open(extract_file_name,"w+")

import pickle
pickle.dump(features, f)
#f.write(word_n_grams)
f.close()
print "File with features created.\n"
print "Program done.\n"




