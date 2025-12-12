# Loops in Python

# Python For Loops

"""This script demonstrates the use of for loops in Python"""
"""
for i in range(1, 11):  # Loop from 1 to 10
    print(f"2 * {i} = {2 * i}")
"""

"""
for i in range(2, 11):  # Loop from 1 to 5
    for j in range(1, 11):  # Loop from 1 to 10
        print(f"{i} * {j} = {i * j}")
"""

"""Another example of iterating through a list"""
"""
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)
"""


"""
for i in range(2, 11):  # Loop from 1 to 5
    for j in range(1, 11):  # Loop from 1 to 10
        print(f"{i} * {j} = {i * j}")
"""

# Python While Loops

i = 1
while i <= 5:
    print(f"2 * {i} = {2 * i}")
    i += 1
else:
    print("Loop is ended")
