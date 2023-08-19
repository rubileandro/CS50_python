import csv

students = []
    
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name":name, "home":home}
        students.append(student)

# Lambda 
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
    