room = input("Choose room (standard/deluxe/suite): ").lower()
nights = int(input("Number of nights: "))

if room == "standard":
    price = 1200
elif room == "deluxe":
    price = 2000
elif room == "suite":
    price = 3500
else:
    print("Room type not available")
    price = 0

if price > 0:
    total = price * nights
    print("Total cost: ₹", total)
