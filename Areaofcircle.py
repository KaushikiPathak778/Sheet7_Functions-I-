# You are given a positive integer A denoting the radius of a circle. You have to calculate the area of the circle.

import math
def circle_area(radius):
    return math.pi*radius*radius
A=int(input())
print(circle_area(A))