#if = do some code only if some conditions is true
# else do something else

age = int(input("enter your age:"))

if age>=100:
    print("you are too old to login..")
elif age >= 18:
    print ("you are now logged in !..")
elif age<0:
    print("age is invalid")
else:
    print("you cant login")