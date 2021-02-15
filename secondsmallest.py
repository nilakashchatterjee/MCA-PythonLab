num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1<num2<num3 or num3<num2<num1:
    small= num2
    print("The second smallest number is:",small)
elif num2<num3<num1 or num1<num3<num2:
    small=num3
    print("The second smallest number is:",small)
else:
    small=num1
    print("The second smallest number is:",small)



