#In this program we are checking whether a number is two digit number
num = input("Enter a number:")
alpha = num.isalpha()
if alpha == False:
    f = float(num)
    i = float(f)
    c=0
    s=0
    sub = f - i
    if sub == 0:
        while f>0:
            r = f % 10
            s = s*10 + r
            f = f // 10
            c+=1
    if c == 2:
        print(f"Entered number {num} is a 2 digit number")
    else:
        print(f"Entered number {num} is not a 2 digit number")
else:
    print("Please enter number as input")