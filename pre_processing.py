import sys
import nltk
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

word_lemmas = []

print "********** Creating a file with n_grams ***************\n"

with open(sys.argv[1]) as f:
	content = f.read()
content = content.decode("utf8")
sent_tokenize = sent_tokenize(content)
for i in sent_tokenize:
	words = word_tokenize(i)
	for j in words:
		word_lemmas.append(wordnet_lemmatizer.lemmatize(j))

#print word_lemmas

word_n_grams = []
word_n_grams_with_spaces = []
max_n_gram_size =6
for i in xrange(len(word_lemmas)-max_n_gram_size+1):
	for j in xrange(max_n_gram_size):
		#print ''.join(word_lemmas[i:i+j+1])
		word_n_grams_with_spaces.append(' '.join(word_lemmas[i:i+j+1]))
		word_n_grams.append(''.join(word_lemmas[i:i+j+1]))

#print word_n_grams
extract_file_name = str(''.join((sys.argv[1]).split('/')[0:-1])) + '/' + str(sys.argv[1]).split('/')[-1:][0].split('.')[0]+"_n_grams.txt"
f= open(extract_file_name,"w+")

import pickle
pickle.dump(word_n_grams, f)
#f.write(word_n_grams)

f.close()
print "File with n_grams created.\n"
print "Program done.\n"
