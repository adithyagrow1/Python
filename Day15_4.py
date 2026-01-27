item = input("Enter item (dosa/idli/pasta/biryani): ").lower()

if item == "dosa":
    print("Price: ₹50")
    print("Options: Masala / Plain")
elif item == "idli":
    print("Price: ₹30")
    print("Options: 2 pcs / 3 pcs")
elif item == "pasta":
    print("Price: ₹120")
    print("Options: White sauce / Red sauce")
elif item == "biryani":
    print("Price: ₹180")
    print("Options: Chicken / Veg / Egg")
else:
    print("Item not found in menu")
