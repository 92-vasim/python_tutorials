########## Tuples ############

fruits = ("banana", "apple", "banana", "mango", 66, 56)

# count method
print(fruits.count("banana"))

# index
print(fruits.index("banana"))

# len
print(len(fruits))

# packing & unpacking 
banana, apple = fruits[:2]
print(banana, apple)