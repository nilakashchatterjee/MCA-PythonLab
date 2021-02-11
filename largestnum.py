# In this program we will print the largest of two number
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))

if num1>num2:
    print(f"The largest number is {num1} ")
elif num2>num1:
    print(f"The largest number is {num2} ")
else:
    print("Both numbers are equal")