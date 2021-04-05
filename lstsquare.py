#QUESTION5
# In this program we are squaring the values of the list
n = int(input("Enter the range of the list:"))
lst1 = [] 
lst2 = [] 
print("Enter the values:")
for i in range(0, n): 
    ele = int(input()) 
    lst1.append(ele) # adding the element to the end of the list
print("The entered list:",lst1)
for i in lst1:
    lst2.append(i**2)
print("Squared of the existing list:",lst2)