travel_class = input("Class (general/sleeper/AC): ").lower()
distance = int(input("Enter distance in km: "))

if travel_class == "general":
    rate = 0.5
elif travel_class == "sleeper":
    rate = 1.0
elif travel_class == "ac":
    rate = 2.0
else:
    rate = 0

if rate == 0:
    print("Invalid class entered")
else:
    total = distance * rate
    print("Ticket Price: ₹", total)
