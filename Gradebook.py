grades = {
    "Sam": "A",
    "Adele": "B",
    "Matt": "C"
}

name = input("Enter student name: ")

if grades.get(name):
    print(grades.get(name))
else:
    print("Student not found.")