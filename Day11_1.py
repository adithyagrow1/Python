email = input("Enter your email: ")

if "@" not in email:
    print("Invalid: Missing @ symbol")

else:
    username, domain = email.split("@")

    if len(username) < 3:
        print("Invalid: Username too short")
    elif "." not in domain:
        print("Invalid: Domain must contain a dot")
    elif not domain.endswith(("com", "in", "edu")):
        print("Invalid: Unapproved domain extension")
    else:
        print("Valid Email")
