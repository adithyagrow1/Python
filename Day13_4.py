name = input("Enter your name: ")
age = input("Enter your age: ")

if not name.isalpha():
    print("Invalid name: Only letters allowed")

elif not age.isdigit():
    print("Invalid age: Numbers only")

elif int(age) < 18:
    print("You must be 18+ to register")

else:
    print("Registration Successful!")
