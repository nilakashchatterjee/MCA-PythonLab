#In this program we will print prime numbers between the given range
lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))
count=0
print("Prime numbers between", lower, "and", upper, "are:",end=" ")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
           count+=1
print("\nTotal prime numbers are:",count)