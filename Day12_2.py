movie = input("Enter movie name: ").lower()
time = input("Enter time (morning/evening/night): ").lower()

if movie == "kalki":
    if time == "morning":
        print("Tickets: ₹150")
    elif time == "evening":
        print("Tickets: ₹200")
    elif time == "night":
        print("Tickets: ₹250")
    else:
        print("Invalid time")
else:
    print("Movie not available")
