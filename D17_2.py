movie = input("Movie Type (U/U-A/A): ").upper()
age = int(input("Enter your age: "))

if movie == "U":
    print("Anyone can watch.")

elif movie == "U-A":
    if age >= 12:
        print("Allowed.")
    else:
        print("Need parental guidance.")

elif movie == "A":
    if age >= 18:
        print("Allowed.")
    else:
        print("Not allowed. 18+ only.")

else:
    print("Invalid movie rating.")
