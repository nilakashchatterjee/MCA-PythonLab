def pattern():
    n= int(input("Enter the number of rows:"))
    
    if n%2==0:  
        for i in range(n):
            for j in range(i+1):
                print("* ",end="")
            print()
        print()
    elif n>3 and n%2!=0:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if(j < i):
                    print(' ', end = '')
                else:
                    print('A', end = '')
            print()
    elif n<=3:
        for i in range(n):
            for j in range(n-i):
                print("A",end="")
            print()
        print() 
    else:
        print("Please enter a valid input....")
    
             

if __name__== "__main__":
    pattern()

