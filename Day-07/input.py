"""
num1 = input("Enter the value of num1:  ")

num2 = input("Enter the value of num2:  ")

total = float(num1) + float(num2)

print("Total is:", total)

"""

# print("The sum of {0} and {1} is {2}".format(num1, num2, total))

# Ask user for the first name and last and print the full name.
"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("Your full name is:", full_name)
"""
"""
first_name = input("First Name: ")
last_name = input("Last Name: ")

full_name = str(first_name) + str(last_name)
print("Full name is: ", full_name)
"""

# f-strings
"""
num1 = input("Enter the value of num1:  ")

num2 = input("Enter the value of num2:  ")

total = float(num1) + float(num2)


# print(f"The sum of {num1} and {num2} is {total}")
print(f"The sum of {num1} and {num2} is {total:.2f}")  # .2f → show 2 decimal places
# f"The total is : {total}"

"""

"""
name = "Sadeed"
age = 30

print(f"My name is {name} and I am {age} years old.")

# Ask user for the first name and last and print the full name using the f-string.

"""

first_name = input("First Name: ")
last_name = input("Last Name: ")

full_name = str(first_name) + " " + str(last_name)
print(f"Full name is: {first_name} {last_name} ")
print(f"Full name is: {full_name} ")
