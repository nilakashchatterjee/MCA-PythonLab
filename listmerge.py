# In this program we are taking input of two arrays, merging them into one and show output of the sorted array
n = int(input("Enter the range of the first list:"))
lst1 = [] 
print("Enter the values:")
for i in range(0, n): 
    ele = int(input()) 
  
    lst1.append(ele) # adding the element to the end of the list
      
print("List 1:",lst1) 
m = int(input("Enter the range of the second list:"))
lst2 = [] 
for i in range(0, n): 
    ele = int(input()) 
  
    lst2.append(ele) # adding the element to the end of the list
      
print("List 2:",lst2)

lst3 = lst1 + lst2
k=sorted(lst3)
print("After Merging List 1 and List 2 we get:",lst3)
print("After Sorting the above List we get:",k)