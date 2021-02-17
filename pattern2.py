# In this program we are printing three different patterns
def pat():
    n = int(input("Enter the number of rows: "))
    num =1  #pattern 1
    for i in range(n):
        for j in range(i+1):
            print(num ,end=" ")
            num +=1
        print()
    print()
    
    k=1  #pattern 2
    j=1
    for i in range(1,n+1):
        print(" "*(n-k) + "O"*(j))
        k+=1
        j+=2
    print("\n")

    m=n  #pattern 3
    p=(n*2)-1
    while m!=0:
        print(" "*(n-m) + "O"*p)
        m-=1
        p-=2
    print("\n")

if __name__ == "__main__": # calling in main function
    pat()