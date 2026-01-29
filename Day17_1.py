name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter password: ")

if not name.replace(" ", "").isalpha():
    print("Invalid name: Only letters allowed.")

elif "@" not in email or "." not in email:
    print("Invalid email format.")

elif len(password) < 8:
    print("Password should be at least 8 characters.")

elif password.isalpha() or password.isdigit():
    print("Password must contain letters + numbers.")

else:
    print("Registration Successful!")
