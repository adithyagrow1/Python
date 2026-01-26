units = int(input("Enter electricity units used: "))

if units <= 100:
    print("Bill Amount: ₹", units * 3)

elif units <= 200:
    print("Bill Amount: ₹", units * 5)

elif units <= 300:
    print("Bill Amount: ₹", units * 7)
    
else:
    print("Bill Amount: ₹", units * 10)
