username = input("Enter username: ")

if len(username) < 5:
    print("Too short")
elif " " in username:
    print("Invalid username")
else:
    print("Valid username")
