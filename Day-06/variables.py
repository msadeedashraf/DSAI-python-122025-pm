"""
x = y = z = "Orange"

print(x)
print(y)
print(z)

"""

"""
# Multiple assignments in a single line
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits

print(y)
print(x)
print(z)

print(fruits[0])

print(fruits[2])

print(fruits[1])
"""

"""
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Welcome"
y = " to"
z = " CBC!"
print(x + y + z)
"""

"""
x = "5"
y = "John"

print(x + y)

x = 5
y = "John"

print(x, y)
"""
# Global variables
"""
x = "Sadeed"


def greeting():
    x = "Krish"
    print("Hello, " + x)
    


greeting()
greeting()
greeting()

print(x)
"""

"""

def addition(num1, num2):
    total = num1 + num2
    # print("Inside the function, total is:", total)
    return total


print(addition(5, 10))

print(addition(20, 10))
print(addition(35, 10))

result = addition(20, 30)
print("Outside the function, result is:", result)
"""


# Global variable
x = "Sadeed"
print(x)


def greeting():
    global x
    x = "Krish"
    print("Hello, " + x)


def welcomemsg():
    print(x, ", Welcome to CBC!")


greeting()
welcomemsg()
