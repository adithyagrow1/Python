pin = input("Enter your 4-digit PIN: ")

if len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN format")

else:
    print("PIN Accepted")
    option = input("Choose option (balance/withdraw/deposit): ").lower()

    if option == "balance":
        print("Your balance is ₹25,000")
    elif option == "withdraw":
        print("Withdrawal successful")
    elif option == "deposit":
        print("Amount deposited")
    else:
        print("Invalid option")
