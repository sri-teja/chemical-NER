import sys
from math import *
from random import shuffle
f=open(sys.argv[1],'r')
content=f.readlines()
g=open('../data/test_features.txt','w')
h=open('../data/train_features.txt','w')
l = len(content)
shuffle(content)

train_data = content[:(l/4)*3]
test_data = content[(l/4)*3:]
print content[0]




for i in test_data:
	g.write("{0}".format(i))
for i in train_data:
	h.write("{0}".format(i))


g.close()
h.close()
f.close()



	
	
	
