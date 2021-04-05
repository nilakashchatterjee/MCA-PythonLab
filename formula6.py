# 8) Python formula to pass value to a formula y=6x^2+3x+2 and prints its outputs
def formula(x):
    y = (6*(x**2))+(3*x)+2
    return y
a = int(input("Enter a value of x:"))
print("The value of the formula is:",formula(a))