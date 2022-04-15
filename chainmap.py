from collections import ChainMap
a={1:'ai',2:'python'}
b={3:'datascience',4:'iot'}
#returning the single view of a and b
c= ChainMap(a,b)
print(c)