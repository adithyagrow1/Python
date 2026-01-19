# Not logical operator

temp = 88
is_sunny = True

if temp <= 25 and not is_sunny:
    print("all set to play..!")
elif temp>100 and not is_sunny:
    print("you'll are cooked")
else:
    print("game has been postponed;")
