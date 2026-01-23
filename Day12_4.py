food = input("Enter food item (pizza/burger/fries): ").lower()

if food == "pizza":
    print("Price: ₹250")
    print("Extra cheese available")
elif food == "burger":
    print("Price: ₹150")
    print("Combo available")
elif food == "fries":
    print("Price: ₹80")
    print("Add mayo for ₹20")
else:
    print("Item not available")
