plate = input("Enter vehicle number plate (e.g., KA03AB1234): ")

if len(plate) != 10:
    print("Invalid plate length")

elif not (plate[0:2].isalpha() and plate[2:4].isdigit() and
          plate[4:6].isalpha() and plate[6:10].isdigit()):
    print("Invalid plate format")

else:
    print("Valid number plate")
