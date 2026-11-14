
students = []

def add_student(name, uid):
    students.append({"name": name, "uid": uid})
    print("Student added successfully!")

def display_students():
    print("Student Records:")
    for student in students:
        print(student["name"], "-", student["uid"])

add_student("Monika", "25MCC20032")
display_students()
