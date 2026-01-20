#conditional expression = A one line shortcut for the if-else statement(ternary operator)
#                         Print or assign one of two values based on a condition
#                         x if condition , else Y

num = 5
a=6
b=7
max_num =a if a>b else b
min_num =a if a<b else b
#print("positive" if num>0 else "Negative")
#result = "Even" if num%2 == 0 else "Odd"
#print(result)

print(f"max_num is {max_num}")
print(f"min_num is {min_num}")