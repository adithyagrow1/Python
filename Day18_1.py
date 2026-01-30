contacts = {}

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Validate Phone Number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ").title()
        number = input("Enter 10-digit phone number: ")

        if len(number) == 10 and number.isdigit():
            contacts[name] = number
            print("Contact saved successfully!")
        else:
            print("Invalid phone number!")

    # Search Contact
    elif choice == "2":
        search = input("Enter name to search: ").title()

        if search in contacts:
            print("Name :", search)
            print("Phone:", contacts[search])
        else:
            print("Contact not found.")

    # Validate Number
    elif choice == "3":
        num = input("Enter number to validate: ")

        if len(num) != 10:
            print("Invalid: length should be 10 digits.")
        elif not num.isdigit():
            print("Invalid: only digits allowed.")
        elif num[0] not in "6789":
            print("Invalid: should start with 6, 7, 8 or 9.")
        else:
            print("Valid phone number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")