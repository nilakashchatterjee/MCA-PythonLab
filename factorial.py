# In this program we are printing the factorial of the given number
num = int(input("Enter a number:"))
if num<0:
    print("Factorial of negetive number is not defined")
elif num==0:
    print("Factorial of 0 is 1" )
else:
    fact=1
    b=num
    while num != 0:
        fact= fact*num
        num-=1
    print(f"Factorial of {b} is {fact}")
    