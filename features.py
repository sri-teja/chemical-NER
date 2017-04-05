import nltk
import sys
import string
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from pre_processing import *
from labeling import *

#given_word = sys.argv[1]
#word_lemma = wordnet_lemmatizer.lemmatize(given_word)
#word_tag = nltk.pos_tag(given_word)

import re
exclude = set(string.punctuation)
#print exclude
ELEMENTS = {
    1: 'H',
    2: 'He',
    3: 'Li',
    4: 'Be',
    5: 'B',
    6: 'C',
    7: 'N',
    8: 'O',
    9: 'F',
    10: 'Ne',
    11: 'Na',
    12: 'Mg',
    13: 'Al',
    14: 'Si',
    15: 'P',
    16: 'S',
    17: 'Cl',
    18: 'Ar',
    19: 'K',
    20: 'Ca',
    21: 'Sc',
    22: 'Ti',
    23: 'V',
    24: 'Cr',
    25: 'Mn',
    26: 'Fe',
    27: 'Co',
    28: 'Ni',
    29: 'Cu',
    30: 'Zn',
    31: 'Ga',
    32: 'Ge',
    33: 'As',
    34: 'Se',
    35: 'Br',
    36: 'Kr',
    37: 'Rb',
    38: 'Sr',
    39: 'Y',
    40: 'Zr',
    41: 'Nb',
    42: 'Mo',
    43: 'Tc',
    44: 'Ru',
    45: 'Rh',
    46: 'Pd',
    47: 'Ag',
    48: 'Cd',
    49: 'In',
    50: 'Sn',
    51: 'Sb',
    52: 'Te',
    53: 'I',
    54: 'Xe',
    55: 'Cs',
    56: 'Ba',
    57: 'La',
    58: 'Ce',
    59: 'Pr',
    60: 'Nd',
    61: 'Pm',
    62: 'Sm',
    63: 'Eu',
    64: 'Gd',
    65: 'Tb',
    66: 'Dy',
    67: 'Ho',
    68: 'Er',
    69: 'Tm',
    70: 'Yb',
    71: 'Lu',
    72: 'Hf',
    73: 'Ta',
    74: 'W',
    75: 'Re',
    76: 'Os',
    77: 'Ir',
    78: 'Pt',
    79: 'Au',
    80: 'Hg',
    81: 'Tl',
    82: 'Pb',
    83: 'Bi',
    84: 'Po',
    85: 'At',
    86: 'Rn',
    87: 'Fr',
    88: 'Ra',
    89: 'Ac',
    90: 'Th',
    91: 'Pa',
    92: 'U',
    93: 'Np',
    94: 'Pu',
    95: 'Am',
    96: 'Cm',
    97: 'Bk',
    98: 'Cf',
    99: 'Es',
    100: 'Fm',
    101: 'Md',
    102: 'No',
    103: 'Lr',
    104: 'Rf',
    105: 'Db',
    106: 'Sg',
    107: 'Bh',
    108: 'Hs',
    109: 'Mt',
    110: 'Ds',
    111: 'Rg',
    112: 'Cp',
    113: 'ut',
    114: 'uq',
    115: 'up',
    116: 'uh',
    117: 'us',
    118: 'uo',
}
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
	mol_count = 0
	molecular_formula = re.findall(r'([A-Z][a-z]*)(\d*)', 'H2SO4')
	for i in molecular_formula:
		if i[0][0] in ELEMENTS:
			mol_count += 1
	molecular_score = mol_count / len(molecular_formula)
	# for generating the n-grams of a token of length less than 4 from start and end
	if len(str1)>3:
		valid = 1
		n_gram = list("12345678")
		n_gram[0] = str1[0:1]
		n_gram[1] = str1[0:2]
		n_gram[2] = str1[0:3]
		n_gram[3] = str1[0:4]
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
	if valid and len(case_pattern):			
		return u, l, c, pun, case_pattern, n_gram, molecular_score

features = {}
for i in word_n_grams:
	
	#uppercase_count, lowercase_count, digit_count, has_punctuation, case_pattern, validity, n_gram = get_features(i)
	l=get_features(i)
	if l:
		features[i] = list(l)
	if i in ans_word_n_grams and i in features:
		features[i].append(1)
	elif i in features:
		features[i].append(0)
#print uppercase_count
#print features
		

extract_file_name = str(''.join((sys.argv[1]).split('/')[0:-1])) + '/' + str(sys.argv[1]).split('/')[-1:][0].split('.')[0]+"_features.csv"
f= open("inputtext/testfile.txt","wa")

for key,val in features.items():
	f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(key.encode('utf-8'),val[0],val[1],val[2],val[3],val[4],val[5].encode('utf-8'),val[6]))

#import pickle
#pickle.dump(features, f)
#f.write(word_n_grams)
f.close()

print features

print "File with features created.\n"
print "Program done.\n"




