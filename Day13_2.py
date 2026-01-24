acc = input("Enter account type (savings/current/salary): ").lower()


if acc == "savings":
    print("Interest rate: 3.5%")

elif acc == "current":
    print("Interest rate: 0%")

elif acc == "salary":
    print("Interest rate: 2%")

else:
    print("Unknown account type")
