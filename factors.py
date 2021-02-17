# In this program we will print the factors of the given number
num = int(input("Enter a number:"))
i=1
n=num
print(f"The factors of {num} are:",end="")
while i<=num:
    if n%i==0:
        print(i,end=" ")
    i+=1
