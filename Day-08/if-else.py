# Python Conditions and If statements

"""
a = input("Enter value for a: ")
b = input("Enter value for b: ")

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

"""

"""Python Logical Operators"""
"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
"""

"""
a = 200
b = 33
c = 100
if a > b and c > a:
    print("Both conditions are True")
else:
    print("At least one condition is False")
"""

"""
a = 200
b = 33
c = 100
if a > b or c > a:
    print("Both conditions are True")
else:
    print("At least one condition is False")
"""

"""
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
else:
    print("a is less than b")

"""

"""
age = 12
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
"""

"""Complex Condition Example"""
"""
temperature = 25
is_raining = True
is_weekend = False

if temperature > 20 and not is_raining or is_weekend:
    print("Great day for outdoor activities!")
else:
    print("Not a Great day for outdoor activities!")
"""

"""Nested If Statements"""

"""
x = 11

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("10 or below.")

"""

score = 85
attendance = 82
submitted = False

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")
