my_dict= {'sreeja':'74','shivani':'75','anusha':'79'}
print(my_dict)
print(type(my_dict))
#function as value
new_dict=dict()
print(new_dict)
print(type(new_dict))
#specifying values as parameters
new_dict=dict(sreeja='74',shivani='75')
print(new_dict)
#accessing functions
print(my_dict['sreeja'])
print(my_dict.values())
print(my_dict.get('anusha'))
#looping
for x in my_dict:
    print(x)
#accessing all the values in the dict
for x,y in my_dict.items():
    print(x,y)
#updating the dict
my_dict['sreeja']='574'
my_dict['anusha']='579'
my_dict['shivani']='575'
print(my_dict)
#deleting
my_dict.pop('sreeja')
print('my_dict')
my_dict.popitem()
print(my_dict)
del my_dict['shivani']
print(my_dict)




