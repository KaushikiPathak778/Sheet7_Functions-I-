# You are given a positive integer A denoting the radius of a sphere. You have to calculate the volume of the sphere.
# Volume of a sphere having radius R is given by (4 * π * R3) / 3.

import math
def sphere_volume(R):
    return (4*math.pi*R**3)/3
A=int(input())
print(sphere_volume(A))