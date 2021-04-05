# QUESTION10
# Concatenate two lists in the following order.
# Input: L1=[1,2] L2=[4,5]
# Output: L3=[(1,4),(1,5),(2,4),(2,5)]
from itertools import product
l1 = [1, 2]
l2 = [4,5]
print("Lists are:",l1,l2)
c_product = product(l1,l2)

c_list = list(c_product)

print("List after concatenation:",c_list)
