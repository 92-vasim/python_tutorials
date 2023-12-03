####### Functions ####### 
""" 
Function = Program 
Program = Set of organized instructions/tasks

() = parameters/arguments 

DRY principle
DRY = Do not Repeat Yourself
1. Define a function
2. Calling a function 
"""

# Simple function 
def greet():
    print("Hello World")

# Function with parameters
# x = 5
# y = 10
# print(x+y)

def add(x, y):
    print(x+y)


# add(5, 10)
# add(4, 6)
# add(6, 30)
# add()

def greet_to(name):
    print(f"Hello, {name}")


# Function with default parameters
def subtract(x=5, y=6):
    print(f"Subtraction of x and y is {x-y}")

# subtract()
# subtract(x=50, y=30)
# subtract(50,30)

invitation1 = ["Subhan", "Azeez", "Faiz"]
invitation2 = ["Vasim", "Sohail", "Moosa"]
invitation3 = ["Abdul", "Jahangir", "Nizam"]
invitations = [invitation1, invitation2, invitation3]


username1 = input("Enter your invitation1 name: ")
username2 = input("Enter your invitation2 name: ")
username3 = input("Enter your invitation3 name: ")
usernames = [username1, username2, username3]

def validate_user(username, invited_names):
    if username in invited_names:
        print(f"You are invited, Mr {username}")
    else:
        print(f"Begane ki shadi mein {username} Diwana")


# validate_user(username1, invitation1)
# validate_user(username2, invitation2)
# validate_user(username3, invitation3)

# def validate_users(usernames, invitations):
#     for username in usernames:
#         for invitation in invitations:
#             if username in invitation:
#                 print(f"You are invited, Mr {username}")
#             else:
#                 print(f"Begane ki shadi mein {username} Diwana")

def validate_users(usernames, invitations):
    for i, username in enumerate(usernames):
        if username == invitations[i]:
            print(f"You are invited, Mr {username}")
        else:
            print(f"Begane ki shadi mein {username}")

validate_users(usernames, invitations)
            


    

