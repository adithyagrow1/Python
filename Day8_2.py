#exercise temperature conversion program.

temp = float(input("enter the temperature:"))
unit = input("is the temperature in F OR C:")

if unit == "F":
    temp = (temp*9/5)+32
    unit = "C"
elif unit == "C":
    temp = (temp-32)*5/9
    unit = "F"
else:
    print("temperature is invalid!")

print(f"your temperature is :{round(temp,2)}{unit}")