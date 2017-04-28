import nltk
import sys
import string
from nltk.stem import WordNetLemmatizer
#from joblib import Parallel, delayed
#import multiprocessing
from nltk import pos_tag
wordnet_lemmatizer = WordNetLemmatizer()

from pre_processing import *
from labeling import *
from read_sdf import *

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

pre_3 = open('../data/prefix_3','r').readlines()
pre_3= [pre_3[i].strip() for i in range(0,len(pre_3))]
pre_4 = open('../data/prefix_4','r').readlines()
pre_4= [pre_4[i].strip() for i in range(0,len(pre_4))]
suf_3 = open('../data/suffix_3','r').readlines()
suf_3= [suf_3[i].strip() for i in range(0,len(suf_3))]
suf_4 = open('../data/suffix_4','r').readlines()
suf_4= [suf_4[i].strip() for i in range(0,len(suf_4))]
#with open('chemtionary.txt') as f:
#	content = f.readlines()

#chemtionary = content 
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
	prefix=0
	suffix=0
	detect_chem_names = [s for s in chem_names if str1.lower() in s.lower()]
	if len(detect_chem_names) > 0:
		chem_name_detected = 1
	else:
		chem_name_detected = 0
	molecular_formula = re.findall(r'([A-Z][a-z]*)(\d*)', str1)
	for i in molecular_formula:
		if i[0] in ELEMENTS.values():
			mol_count += 1
	try:
		molecular_score = float(mol_count) / float(len(molecular_formula))
	except:
		molecular_score = 0
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

		#if ''.join(e for e in str1 if e.isalpha()) in chemtionary:
		#	pid = 1
		#else:
		#	pid = 0
	#print str1[:3]

	if str1[:3] in pre_3 or str1[:4] in pre_4:
		prefix=1
	if str1[-3:] in suf_3 or str1[-4:] in suf_4:
		suffix=1
	postag=pos_tag([str1])[0][1]
	if valid and len(case_pattern):			
		l=[str1,u, l, c, pun, case_pattern, n_gram, molecular_score,prefix,suffix, chem_name_detected,postag]
		if str1 in ans_word_n_grams:
			l.append(1)
		else:
			l.append(0)
		return l


#for i in word_n_grams:
	
	#uppercase_count, lowercase_count, digit_count, has_punctuation, case_pattern, validity, n_gram = get_features(i)
#	l=get_features(i)
#	if l:
#		features[i] = list(l)
#	if i in ans_word_n_grams and i in features:
#		features[i].append(1)
#	elif i in features:
#		features[i].append(0)
#print uppercase_count
#print features
		

#extract_file_name = str(''.join((sys.argv[1]).split('/')[0:-1])) + '/' + str(sys.argv[1]).split('/')[-1:][0].split('.')[0]+"_features.csv"
f= open(sys.argv[2],"w")
from multiprocessing import Pool
p = Pool(12)

val_list= p.map(get_features, word_n_grams)

for val in val_list:
	#val= get_features(i)
	#print len(features)
	if val:
		f.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\n".format(val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7], val[8],val[9],val[10],val[11],val[12]))

#import pickle
#pickle.dump(features, f)
#f.write(word_n_grams)
f.close()

#print features

print "File with features created.\n"

