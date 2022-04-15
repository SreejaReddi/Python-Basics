import array as arr
a=arr.array('u',['s','r','e','e','j','a'])
print(a)
#accessing elements
print(a[2],a[5])
#length of an array
print(len(a))
#adding one element in the end
a.append('r')
print(a)
#adding one or more elements in the end
a.extend(['e','d','y'])
print(a)
#adding an element at a preferred position
a.insert(9,'d')
print(a)
#removing elements using pop without using parameters
a.pop()
print(a)
#removing elements with parameters
a.pop(9)
print(a)
#removing using remove
a.remove('s')
print(a)
#using negative index values removes the last value in the array
a.pop(-1)
print(a)
#slicing an array
print(a[0:3])
