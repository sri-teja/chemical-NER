import sys
f = open(sys.argv[1], 'r')
content = f.readlines()
for i in content:
	if len(i.split('\t'))!=11:
		print i

