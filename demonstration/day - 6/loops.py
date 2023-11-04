""" 
1. Print 1 to 100 

"""
# Variable defining
# value = 2 
# print(f"value: {value}")

# # Updating variable 
# # value = 5 
# # print(f"value: {value}")

# # Updating variable 
# # value = value + 5 
# value += 5 
# print(f"value: {value}")

""" 
while (condition):
    statement 

"""

count = 100
while count < 200:
    print(f"Count is {count}")
    count += 2

value = 0 
while True: 
    print(f"Value: {value}")
    value += 1 

###### For loop 


""" 
1. Iteration (operation of loop)
2. Iterable - variable (non primitive-list-dictionary-tuple-set)

in: mostly used on iterables 

"""

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)

""" 
1. in - used on iterables 
2. range - function (generator)

"""
# values = [1, 2, 3, 4, 5, 6]
for i in range(1, 100):
    print(i)