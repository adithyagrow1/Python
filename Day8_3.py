#logical operators = evaluate multiple conditions(or,and,not)
# or = at least one condition must be true
# and = both the conditions must be true
# not = inverse the condition.

temp = 26
is_raining= False

if temp>25 or temp<0 or is_raining :
    print("the outdoor event can not be conducted!")
else:
    print("lessgooo! the outdoor event will start!")