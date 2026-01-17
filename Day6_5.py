# to calculate the hypotenuses of a triangle.
import math
A = float(input("enter side A:"))
B = float(input("enter side B:"))

hypotenuses = math.sqrt(pow(A,2)+pow(B,2))

print(f"the hypotenuses of the given right angle triangle is:{round(hypotenuses,2)}cm^2 ")