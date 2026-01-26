amount = float(input("Enter total amount: "))
coupon = input("Enter coupon code: ").upper()

if coupon == "DISCOUNT10" and amount >= 500:
    print("Coupon applied! You got 10% off.")

elif coupon == "SUPER20" and amount >= 1000:
    print("Coupon applied! You got 20% off.")

elif coupon == "SUPER20" and amount < 1000:
    print("Add items worth ₹", 1000 - amount, "to use this coupon.")

else:
    print("Invalid or expired coupon.")
