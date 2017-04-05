import sys
from xml.etree.ElementTree import ElementTree
tree = ElementTree()
itree = tree.parse(sys.argv[1])

print itree.findall("{http://www.ncbi.nlm.nih.gov}PC-Compound")
#print tree.findall('PC-Compounds')
for compound in itree.findall("{http://www.ncbi.nlm.nih.gov}PC-Compound"):
	for info_data in compound.findall("{http://www.ncbi.nlm.nih.gov}PC-Compound_props/{http://www.ncbi.nlm.nih.gov}PC-InfoData"):
		label = info_data.find("{http://www.ncbi.nlm.nih.gov}PC-InfoData_urn/{http://www.ncbi.nlm.nih.gov}PC-Urn/{http://www.ncbi.nlm.nih.gov}PC-Urn_label").text
		name = ""
		try:
			name = info_data.find("{http://www.ncbi.nlm.nih.gov}PC-InfoData_urn/{http://www.ncbi.nlm.nih.gov}PC-Urn/{http://www.ncbi.nlm.nih.gov}PC-Urn_name").text
		except:
			pass
		if label=="IUPAC Name" and (name=="Systematic" or name=="Traditional") :
			sys_name = info_data.find("{http://www.ncbi.nlm.nih.gov}PC-InfoData_value/{http://www.ncbi.nlm.nih.gov}PC-InfoData_value_sval").text
			for j in sys_name.split(" "):
				print ''.join(e for e in j if e.isalpha())
			print ''.join(e for e in sys_name if e.isalpha())
			


#for child in root:
#	print child.tag, child.attrib


