# In this program we will print the table multiplication
n = input("Enter a number:")
if n.isnumeric() == True:
    num = int(n)
    if num >= 1:
        for i in range(1,11):
            print(num,"x",i,"=",num*i)
    else:
        print("Enter a number greater than zero")
else:
    print("Please enter a positive integer value...")