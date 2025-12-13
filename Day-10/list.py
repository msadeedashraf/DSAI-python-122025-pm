"""
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

print("List of students:")
print(students[0])  # Accessing first element
print(students[1])  # Accessing second element
print(students[2])  # Accessing third element

print(students[-1])  # Accessing last element


print(students[len(students) - 1])  # Accessing last element using length

print("Total number of students:", len(students))

# Iterating through the list of students
print("Iterating through the list of students:")
for student in students:
    print(student)
"""

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:3])
"""

students = ["Alice", "Bob", "Charlie", "David", "Eva"]
students[1:3] = ["Ben", "Cathy"]  # Modifying elements at index 1 and 2
for student in students:
    print(student)

students.append("Frank")  # Adding a new student at the end
for student in students:
    print(student)

students.insert(2, "Grace")  # Inserting a new student at index 2
for student in students:
    print(student)

students2 = ["Hannah", "Ian"]
students.extend(students2)  # Extending the list with another list
for student in students:
    print(student)


print("Print sorted list of students")

students.sort()  # Sorting the list of students
for student in students:
    print(student)

# Python - List Methods
# https://www.w3schools.com/python/python_lists_methods.asp

# https://www.w3schools.com/python/python_lists_exercises.asp
