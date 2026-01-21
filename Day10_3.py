text = input("Enter text: ")

has_digit = False


for char in text:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("Contains number")
else:
    print("Only letters")
