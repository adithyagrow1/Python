msg = input("Type your calculation request: ").lower()

if "add" in msg or "sum" in msg:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a + b)


elif "subtract" in msg or "minus" in msg:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a - b)


elif "multiply" in msg or "product" in msg:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Answer =", a * b)


elif "divide" in msg:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Answer =", a / b)


else:
    print("Sorry, I couldn't understand the operation.")