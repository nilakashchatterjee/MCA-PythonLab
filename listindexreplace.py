# In this program we are finding the index where the value is 0 and replacing second last element of the list with new one
l1=[20,0,'abc',50,12.8]
k=0
print("Before checking and replacing:",l1) # before checking and replacing
for i in range(len(l1)):
    if l1[i] == 0:
        k=i # fetching the index
print("Index where zero is found:",k)
l1[-2]="replaced"
print("After checking and replacing:",l1) # after checking and replacing