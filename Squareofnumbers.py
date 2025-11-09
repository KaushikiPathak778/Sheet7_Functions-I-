# WAP to print square of all numbers from x to y.

def print_squares(x,y):
    for num in range(x,y+1):
        print(f"{num} squared is {num**2}")
x=int(input("Enter starting number(x): "))
y=int(input("Enter ending number(y): "))
print_squares(x,y)