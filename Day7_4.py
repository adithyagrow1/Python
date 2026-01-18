#Python calculator

a = float(input("enter the number A:"))
operator = input("enter the operator(+ - * /):")
b = float(input("enter the number B:"))

if operator =="+":
    answer = a+b
    print(f"{a}+{b}={answer}:")
elif operator =="-":
    answer = a-b
    print(f"{a}-{b}={answer}:")
elif operator =="*":
    answer = a*b
    print(f"{a}*{b}={answer}:")
elif operator =="/":
    answer = a/b
    print(f"{a}/{b}={round(answer,2)}")
else:
    print("invalid request..")

