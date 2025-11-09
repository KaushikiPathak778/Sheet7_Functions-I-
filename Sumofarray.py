# Write a program to print sum of elements of the input array A of size N.

def array_sum(A):
    return sum(A)
N=int(input())
A=list(map(int, input("Enter array elements separated by space: ").split()))
print("Sum of elements:",array_sum(A))