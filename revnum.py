#this program reverses the input number from user 
def rev(n): #function definition
    r=0  
    while(n>0):
        a = n % 10
        r = r * 10 + a  #saving the reversed number
        n = n // 10
    return r
num = float(input("Enter the number: "))
reverse = rev(num) #function calling
print(f"The reverse of {num} is {reverse}")

