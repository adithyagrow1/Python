# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students available.")
        return
    print("\nRoll\tName\tMarks\tGrade")
    for roll, data in students.items():
        grade = calculate_grade(data["marks"])
        print(f"{roll}\t{data['name']}\t{data['marks']}\t{grade}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        data = students[roll]
        print("Name:", data["name"])
        print("Marks:", data["marks"])
        print("Grade:", calculate_grade(data["marks"]))
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        students[roll]["name"] = input("Enter new name: ")
        students[roll]["marks"] = float(input("Enter new marks: "))
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
