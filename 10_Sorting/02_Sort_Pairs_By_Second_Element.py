students = [
    ("Alice", 85),
    ("Bob", 70),
    ("Charlie", 95),
    ("David", 80)
]

students.sort(key = lambda x: x[1])
print(students)