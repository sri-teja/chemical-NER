import csv

f = open('./inputtext/ninefilefeatures.txt', 'rb')
reader = csv.reader(f,delimiter='\t')

for row in reader:
	if(len(row)!=8):
		break	
	else:
		for i in row:
			if(i==''):
				print row
				break
