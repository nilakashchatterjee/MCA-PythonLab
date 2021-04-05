# 10) Calculate the a list for the function x = n^2 + 1
def sequence(alst):
    for i in range(len(alst)):
        alst[i] = (alst[i] ** 2) + 1

lst = [2,4,3,8,12]
print("Original List:",lst)
sequence(lst)
print("List after applying the formula:",lst)