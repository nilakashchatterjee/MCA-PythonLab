# 5) Python function add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def string(st):
    l = len(st)
    if l > 2:
        if st[-3:] == "ing":
            st += "ly"
        else:
            st += "ing"
    return st
a = input("Enter a string:")
print(string(a))