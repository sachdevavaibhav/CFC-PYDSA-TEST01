# 1. Write a Python program which accepts the radius of a circle from the user
# and compute the area.
import math

radius = float(input("Enter radius of circle in cm: "))

area = round(math.pi*radius**2, 2)

print(area, 'cm square')