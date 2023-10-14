####### list 

## list of strings 
fruits = ["banana", "apple", "aam", "shehtoot"]
print(f"These are available fruits in our shop: {fruits}")

## list of integers 
marks = [45, 74, 83, 56, 23]
print(f"Marks of samdani institute students are: {marks}")

## combined 
combined = ["charminar", 8, True, "9"]

print("#"*20)
# Accessing element 
print(fruits[1])
print(fruits[-1])


print("#"*20, "\n")
print("List methods/functions")

# append: insertion of value in last position
print(fruits)
fruits.append("kairi")
print(fruits)

# insert: insertion of value with specific position
print("#"*20, "\n")
print(fruits)
fruits.insert(1,"grapes")
print(fruits)

# remove: remove an element with specifying the value 
print("#"*20, "\n")
print(fruits)
fruits.remove("kairi")
print(fruits)

# pop: remove an element with specifying the index 
print("#"*20, "\n")
print(fruits)
# fruits.pop()
fruits.pop(1)
print(fruits)

# len: 
print("#"*20, "\n")
print(fruits)
print(len(fruits))

# sort: 
print("#"*20, "\n")
print(fruits)
fruits.sort()
print(fruits)

# reverse: 
print("#"*20, "\n")
print(fruits)
fruits.reverse()
print(fruits)

