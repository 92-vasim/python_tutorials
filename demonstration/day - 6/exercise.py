""" 
1. Tuples 
2. Dictionaries
3. Sets 
4. Operators 
5. Conditional statements
"""

""" 
1. Use tuples and all methods 
2. Use dictionaries and all methods
3. Use sets and all methods
4. Conditional statement one example of driving 
"""

# print(f"---Welcome to driving test---")
# age = int(input("Enter your age: "))

# print(f"Your age is {age}")

# if age < 18:
#     print("Hello")

# else:
#     print("World")


""" 
if (condition):
    true statement 
else:
    false statement 

    
if (condition):
    true statement 
elif (condition):
    true statement 
else:
    false statement 

- start with greater value 
    
"""

print(f"---Welcome to driving test---")
age = int(input("Enter your age: "))

if age > 70:
    print("You are senior citizen")
elif age > 18:
    print("You are major")
elif age < 18:
    print("You are minor")

print("----Welcome to Rumaan Inaugration----")
username = input("Please enter your invitation name: ")

invited = ["vasim", "faiz", "subhan"]

print(type(invited))

if username == invited[0]:
    print(f"Welcome to Rumaan Inaugration Party {username}")
else:
    print(f"Begane ki shadi mein {username} diwana")


###### Logical operators ########
""" 
and 
or 
not
"""

print(f"---Welcome to existance test---")
age = int(input("Enter your age: "))


"""if age > 70:
    if age < 120:
        print(f"You are senior citizen. Because your age is {age}")"""

if age > 70 and age < 120:
    print(f"You are senior citizen. Because your age is {age}")
else:
    print("Sorry you do not exist.")