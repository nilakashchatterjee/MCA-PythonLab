# 1) Python function that takes a string as a parameter and returns a string with every successive repetitive character replaced with *
def fun(str1):
    new_str = ""
    for i in str1:
        if i in new_str:
            new_str += "*"
        else:
            new_str += i
    return new_str

print(fun("Hello World"))
print(fun("Balloon"))
