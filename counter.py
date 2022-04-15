from collections import Counter
a=[1,2,2,3,3,4,5,5,5,6,7,7,7,8]
#counting the values in the list
count=Counter(a)
print(count)
#returning all the values in the list
print(list(count.elements()))
#values count in a sorted order
print(count.most_common())
#subtracting the value
sub={2:2,7:2}
print(count.subtract(sub))
print(count.most_common())