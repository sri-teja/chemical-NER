f=open('../data/chemtionary.txt','r')
content=f.readlines()
prefix_3={}
prefix_4={}
suffix_3={}
suffix_4={}
for i in content:
	if i[:3] in prefix_3.keys():
		prefix_3[i[:3]]+=1
	else:
		prefix_3[i[:3]]=1
	if i[:4] in prefix_4.keys():
		prefix_4[i[:4]]+=1
	else:
		prefix_4[i[:4]]=1
	if i[-4:-1] in suffix_3.keys():
		suffix_3[i[-4:-1]]+=1
	else:
		suffix_3[i[-4:-1]]=1
	if i[-5:-1] in suffix_4.keys():
		suffix_4[i[-5:-1]]+=1
	else:
		suffix_4[i[-5:-1]]=1
f=open('../data/prefix_3','w')
for i in prefix_3.keys():
	f.write("{0}\n".format(i))
f=open('../data/prefix_4','w')
for i in prefix_4.keys():
	f.write("{0}\n".format(i))
f=open('../data/suffix_3','w')
for i in suffix_3.keys():
	f.write("{0}\n".format(i))
f=open('../data/suffix_4','w')
for i in suffix_4.keys():
	f.write("{0}\n".format(i))
