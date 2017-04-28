import sys
import os

## path to sdf file
sdf_file = '../data/ChEBI.sdf'

## reading the sdf file
f = open(sdf_file, 'r')

## list of lines
content =  f.readlines()

## variable helps to save the next line of the desired pattern
name = 0
syn_came = 0
## save the desired names in this list
chem_names = []

## iter through the list of lines and access each line
for i in content:
	i = i.strip()
	#if i == "> <CAS Registry Numbers>":
	#	syn_came = 0
	## desired words
	if name == 1:
		if i :
			chem_names.append(i)
			name = 0
	## desired pattern
	if i == "> <ChEBI Name>" or i == "> <Formulae>" or i =="> <IUPAC Names>" or i=="> <Synonyms>":
		name = 1
	else:
		name = 0

print len(chem_names)
print "Success : Names extracted from sdf file"

