age = int(input("Enter your age: "))

"""
if (condition) {
    statement
}
"""
# 1-if
# if age>18:
#     print("You can drive.")


## 2-if-else
# if age>18:
#     print("You can drive.")

# else:
#     print("You can not drive.")

## 3-if-else-if
# if age<18:
#     print("Minor")

# elif age>18:
#     print("Major")

""" 
Start using greater value in conditions.
"""

## 4-example
if age>70:
    print("Senior")
elif age>18:
    print("Major")
elif age<18:
    print("Minor")