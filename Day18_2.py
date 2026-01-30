library = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book by Title")
    print("3. Check Availability")
    print("4. Exit")
    option = input("Enter choice: ")
    # Add Book
    if option == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        status = input("Is the book available? (yes/no): ").lower()
        if status not in ["yes", "no"]:
            print("Invalid status.")
        else:
            library.append({"title": title, "author": author, "available": status})
            print("Book added successfully!")
    # Search Book by Title
    elif option == "2":
        keyword = input("Enter keyword to search: ").lower()

        found = False
        for book in library:
            if keyword in book["title"].lower():
                print("\nFound:")
                print("Title :", book["title"])
                print("Author:", book["author"])
                print("Available:", book["available"])
                found = True

        if not found:
            print("No book found with that keyword.")

    # Check Availability
    elif option == "3":
        title = input("Enter full book title: ").strip().lower()
        found = False
        for book in library:
            if title == book["title"].lower():
                print("Status:", "Available" if book["available"] == "yes" else "Not Available")
                found = True
        if not found:
            print("Book not found in library.")
    elif option == "4":
        print("Exiting system…")
        break
    else:
        print("Invalid option. Try again.")