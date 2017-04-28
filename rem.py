import os
import shutil
from os import listdir
from os.path import isfile, join

l = listdir('crfpp')
p = listdir('.')
for i in p:
	if i in l:
		if isfile(i):
			os.remove(i)
		else:
			shutil.rmtree(i)
