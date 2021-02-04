# In this program we will check a number whether it is divisible by both 3 and 5
num = float(input("Enter a number:"))
if num%3 == 0 and num%5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")