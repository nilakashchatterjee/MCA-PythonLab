n = int(input("Enter the range of the set:"))
lst = [] 
print("Enter the values:")
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) # adding the element to the end of the list
s = set(lst)
print("The set is:",s)
s.pop()
print("After the deletion an element of the set:",s)
s.add(6)
print("After the addtion of new element of the set:",s)
