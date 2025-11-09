# Given a number A. Return square root of the number if it is perfect square otherwise return -1.
# Note: A number is a perfect square if its square root is an integer.

import math
def perfect_square_root(A):
    sqrt_A=math.isqrt(A)
    if sqrt_A*sqrt_A==A:
        return sqrt_A
    else:
        return -1
A=int(input())
print(perfect_square_root(A))