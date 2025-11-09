# Given the lengths of semi-major axis A and semi-minor axis B of an ellipse
# Calculate the Area of the Ellipse.
# Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π*a*b.

import math
def ellipse_area(a,b):
    return math.pi*a*b
A=float(input())
B=float(input())
print(ellipse_area(A,B))