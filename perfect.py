# In this program we are going to find perfect number using function
def perfect(n): #function
    i=1
    s=0
    while i<n:
        if n%i==0:
            s=s+i
            
        i+=1
    return s
# Driver code
n = int(input("Enter a number:"))
no = perfect(n)
if n == no:
    print("It is a perfect number")
else:
    print("It is not a perfect number")