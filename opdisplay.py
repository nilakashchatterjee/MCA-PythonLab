# Here we are taking number and operator to perform the specific operation

a = float(input("Enter 1st Number: ")) #1st number
b = float(input("Enter 2nd Number: ")) #2nd number
op = input("Enter operator: ") # taking the operator

if op == "+":
    add = a + b
    print("Result:",add)

elif op == "-":
    sub = a - b
    print("Result:",sub)

elif op == "*":
    mul = a * b
    print("Result:",mul)

elif op == "/":
    if b != 0:
        div = a / b
        print("Result:",div)
    else:
        print("Error!!!\nCannot divide by zero")

else:
    print("Error!!!\nEnter a basic arithmetic operator")