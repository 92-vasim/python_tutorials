""" 
1. Variable
2. Data type
3. Print function 
4. Input function
5. Comments 
6. Type casting
7. String concatination 
8. String 
"""

########## Strings #########

myname = "vasim" 
# print(myname)

location = "bahadurpura"
age = 23

# print("My name is " + myname + " and age is " + str(age) + " and my location is " + location)


######## escape sequences

desc = "My name is Mohammed Vasim. \tI don't have iPhone."

# print("My name is Mohammed Vasim. \nI don't have iPhone.")
# print(desc)


######### String concatenation #########
firstname = "Mohammed"
lastname = "Vasim"

fullname = firstname + " " + lastname
# print(fullname)


############ String interpolation - f-strings #########

myname = "vasim" 
# print(myname)

location = "bahadurpura"
age = 23

# print("My name is " + myname + " and age is " + str(age) + " and my location is " + location)

profile1 = f"My name is {myname} and age is {age} and my location is {location}"
# print(profile1)

profile2 = "My name is {} and age is {} and my location is {}".format(myname, age, location)
# print(profile2)


######### String slicing #########
# indexing starts from 0
# 0=1

fullname = "Mohammed Vasim"

# extracting from "M" to "m"
print(fullname[0:5])


# extracting from "h" to "m"
print(fullname[2:5])

# extracting from starting to "m"
print(fullname[:5])

# extracting from "m" to end
print(fullname[5:])

# mohammed
# 01234567  - indexing 

# slicing reverse 
print(fullname[-1])

# slicing reverse 
print(fullname[-5:])

# slicing with skipping 
print(fullname[::3])