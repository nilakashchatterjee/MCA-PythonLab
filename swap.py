#program to swap the values of two variables
c = input("Enter the value in C: ")
d = input("Enter the value in D: ")

print("\nValues before interchanging:\n"
        f"C={c}; D={d}")

c,d=d,c #interchanging the values of C and D

print("\nValues after interchanging:\n"
        f"C={c}; D={d}")