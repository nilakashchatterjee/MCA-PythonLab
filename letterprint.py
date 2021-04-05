# 3) Python function which take input a string and return a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
def letter(ltr):
    if len(ltr)<4:
        print("Enter a string with minimum 4 characters")
    elif len(ltr)==4:
        print(ltr)
    else:
        print(ltr[:2] + ltr[-2:])
a = input("Enter a string:")
letter(a)