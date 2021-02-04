num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1<num2 and num1<num3:
    small=num1

elif num2<num1 and num2<num3:
    small = num2

else:
    small = num3

if num1>small and num1<num3:
    ssmall = num1
elif num2>small and num2<num3:
    ssmall = num2
else:
    ssmall = num3

print("The second smallest number is:",ssmall)