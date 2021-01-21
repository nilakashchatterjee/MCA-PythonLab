#this program calculates the simple interest
p = float(input("Enter the principle amount: ")) 
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
print("\nThe given values are:\n"  #displaying all the entered values
        f"Principle: {p} \n"
        f"Rate of interest: {r} % \n"
        f"Time period: {t} \n")

i = (p*r*t)/100 #calulating the simple interest
print("The amount of interest is",i)