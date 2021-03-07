# In this program we are implementing the palindrome number
num=int(input("Enter a number:"))
temp=num
rev=0

while(num>0):
    digit=num%10
    rev= rev*10+digit #storing the reversed number
    num //=10

if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")