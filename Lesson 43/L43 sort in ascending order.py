import numpy as np

data_type = [("name", "S15"), ("grade", int), ("weight", float)]

students_details = [("Austin", 5, 42.3), ("Lerroy", 1, 37.9), ("Paul", 10, 65.7), ("Barret", 3, 40.1)]

#create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array: ")
print(students)
print()

print("Sort by weight: ")
print(np.sort(students, order="weight"))