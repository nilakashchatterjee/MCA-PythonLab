# Here we will distinguinh between the equilateral,isosceles and scalene triangle
print("...Enter the three sides of a triangle...")
a,b,c = float(input()),float(input()),float(input())
if a==b and b==c and c==a:
    print("It is an equilateral triangle")
elif a==b or b==c or c==a:
    print("It is an isosceles triangle")
else:
    print("It is an scalene triangle")
