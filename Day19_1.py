students = ["Adithya", "Merin", "Rahul", "Riya", "Manoj"]
attendance = {}

while True:
    print("\n--- SMART ATTENDANCE SYSTEM ---")
    print("1. Mark Attendance")
    print("2. Check Attendance by Name")
    print("3. Show All Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Mark Attendance
    if choice == "1":
        name = input("Enter student name: ").title()

        if name not in students:
            print("Student not found in class list.")
        else:
            status = input("Present or Absent? ").lower()
            if status not in ["present", "absent"]:
                print("Invalid status.")
            else:
                attendance[name] = status
                print(name, "marked as", status)


    # Check Attendance
    elif choice == "2":
        name = input("Enter name to check: ").title()

        if name in attendance:
            print(name, "is", attendance[name])
        else:
            print("Attendance not marked for", name)

    # Show All
    elif choice == "3":
        if not attendance:
            print("No attendance marked yet.")
        else:
            for name, status in attendance.items():1
                print(name, ":", status)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")