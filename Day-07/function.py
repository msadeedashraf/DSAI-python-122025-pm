def add(num1, num2):
    print(f"The result after adding {num1} and {num2} is  {(num1+num2):.2f}")


def subtract(num1, num2):
    print(f"The result after subtracting {num1} and {num2} is  {(num1-num2):.2f}")


def multiply(num1, num2):
    print(f"The result after multiplying {num1} and {num2} is  {(num1*num2):.2f}")


def divide(num1, num2):
    print(f"The result after dividing {num1} and {num2} is  {(num1/num2):.2f}")


a = input("Enter the value of num1:  ")

b = input("Enter the value of num2:  ")


add(float(a), float(b))
subtract(float(a), float(b))
multiply(float(a), float(b))
divide(float(a), float(b))


# Create a function that receives three numbers and calculates the average of those numbers.
