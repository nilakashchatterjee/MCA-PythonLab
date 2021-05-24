# 3) Evaluating a formula square root of [(2*C*D)\H] given value of C and H and Taking comma seperated inputs of D
import math as m
c = 50 # given values 
h = 30 # given values
d = [int(i) for i in input("Enter multiples values:").split(",")]
print("The Output is:",end="")
for i in range(len(d)):
    q = m.sqrt((2*c*d[i])/h)
    print(int(q),end=",")