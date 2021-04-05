# 4) Python function which take two string as input and return a single string from two given strings, separated by a space and swap the first two characters of each string
def charswap(a,b):
    # string slicing
    n_a = b[:2] + a[2:]
    n_b = a[:2] + b[2:]
    return n_a+" "+n_b
print(charswap("abc","xyz"))