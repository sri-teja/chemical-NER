import nltk
import sys
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

given_word = sys.argv[1]
word_lemma = wordnet_lemmatizer.lemmatize(given_word)
word_tag = nltk.pos_tag(given_word)


exclude = set(string.punctuation)
#print exclude

def get_upper_lower_digit_count(str1):
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
		n_gram[0] = str1[0]
		n_gram[1] = str1[0:1]
		n_gram[2] = str1[0:2]
		n_gram[3] = str1[0:3]
		n_gram[4] = str1[-1:]
		n_gram[5] = str1[-2:]
		n_gram[6] = str1[-3:]
		n_gram[7] = str1[-4:]
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

uppercase_count, lowercase_count, digit_count, has_punctuation, case_pattern, validity, n_gram = get_upper_lower_digit_count(given_word)


#print uppercase_count

		




