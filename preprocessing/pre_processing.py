import nltk
import sys
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
word_lemmas = []

with open(sys.argv[1]) as f:
	context = f.readlines()


 
word_n_grams = []
word_n_grams_with_spaces = []
max_n_gram_size =3
words=[]
for k in context:
	#k = k.decode("utf8")
	kl=k.split("\t")
	text = ' '.join(kl[1:])
	sent_tokenizer = sent_tokenize(text)
	for i in sent_tokenizer:
		words1=i.split(' ')
		for j in words1:
			#word_lemmas.append(wordnet_lemmatizer.lemmatize(j))
			words.append(j.strip())

for i in range(len(words)-max_n_gram_size+1):
	for j in range(max_n_gram_size):
		word_n_grams.append(''.join(words[i:i+j+1]))
		#word_n_grams.append(''.join(words[i:i+j+1]))


print "n-grams created."
