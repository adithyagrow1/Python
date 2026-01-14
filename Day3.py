# Bank Account Management System

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts[acc_no] = {"name": name, "balance": balance}
    print("Account created successfully!")

def view_accounts():
    if not accounts:
        print("No accounts found.")
        return
    print("\nAcc No\tName\t\tBalance")
    for acc, data in accounts.items():
        print(f"{acc}\t{data['name']}\t\t{data['balance']}")

def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Deposit successful!")
    else:
        print("Account not found.")

def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount > accounts[acc_no]["balance"]:
            print("Insufficient balance!")
        else:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
    else:
        print("Account not found.")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found.")

while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        check_balance()
    elif choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice!")
