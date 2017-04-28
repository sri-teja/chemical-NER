import sys
f= open(sys.argv[1],'r')
g = open(sys.argv[2],'w')

for i in f:
	l=i.strip().split('\t')
	g.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(l[1],l[2],l[3],l[4],l[7],l[8],l[9],l[10],l[11],l[12]))
