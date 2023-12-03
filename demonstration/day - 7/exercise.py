""" 
1. 3 examples of conditional statements
    a. Dawat 
    b. Age
    c. Gender 

2. 3 examples of loops 
    a. print 1 to 50 using while loop.
    b. create fruits list of 8 elements and print that you like each of them using for loop.
    c. print 1 to 50 using for loop with range.
"""

# Demonstration of the range function
for i in range(1, 6):
    print(i)

###############

invitation = ["Subhan", "Azeez", "Faiz"]

username = input("Enter your invitation name: ")

################

if username == invitation[0]:
    print(f"You are invited, Mr {username}")
elif username == invitation[1]:
    print(f"You are invited, Mr {username}")
elif username == invitation[2]:
    print(f"You are invited, Mr {username}")
else:
    print(f"Begane ki shadi mein {username} Diwana")

#####################

if username in invitation:
    print(f"You are invited, Mr {username}")
else:
    print(f"Begane ki shadi mein {username} Diwana")


##################

for user in invitation:
    if username == user:
        print(f"You are invited, Mr {username}")
    else:
        print(f"Begane ki shadi mein {username} Diwana")


