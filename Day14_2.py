destination = input("Enter destination (Delhi/Mumbai/Bangalore): ").lower()
class_type = input("Enter class (economy/business/first): ").lower()

if destination == "delhi":

    if class_type == "economy":
        print("Ticket Price: ₹3,500")

    elif class_type == "business":
        print("Ticket Price: ₹7,000")

    else:
        print("Ticket Price: ₹12,000")

elif destination == "mumbai":

    if class_type == "economy":
        print("Ticket Price: ₹4,000")

    elif class_type == "business":
        print("Ticket Price: ₹8,000")

    else:
        print("Ticket Price: ₹13,000")

elif destination == "bangalore":

    if class_type == "economy":
        print("Ticket Price: ₹3,000")

    elif class_type == "business":
        print("Ticket Price: ₹6,500")
        
    else:
        print("Ticket Price: ₹11,000")

else:
    print("Destination not available")
