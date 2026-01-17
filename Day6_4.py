# find the area of the circle

import math

radius = float(input("enter the radius of a circle:"))

area = math.pi*radius*radius # or pow(radius,2)

print(f"the area of the circle is {round(area,2)}cm")
