from pubchempy import *

c = Compound.from_cid(1423)
cs = get_compounds('HCL', 'name')
cs1 = get_synonyms('dheeraj', 'name')
print c
print cs
print cs1
