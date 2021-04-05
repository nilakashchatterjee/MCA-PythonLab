# In this program we will replace the first element of a tuple with a new one
t1 = (4,5,6)
print("Elements of tuple before replacing:",t1)
t = list(t1)
t[0] = 1
t1 = tuple(t)
print("Elements of tuple after replacing:",t1)