# Program to display Fibonacci Series upto given range
n = int(input("Enter the number of terms:"))
a,b = 0,1
count = 0
if n <= 0:
    print("\nPlease enter a positve integer")
elif n == 1:
    print("\nFibonacci sequence upto",n,"term:",end=" ")
    print(a)
else:
    print("\nFibonacci sequence upto",n,"terms :",end=" ")
    while count < n:
        print(a,end=" ")
        c = a+b
        a = b
        b = c
        count += 1

