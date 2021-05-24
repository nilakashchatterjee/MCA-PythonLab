# Q1. A “Word” is a sequence of non-space characters which is maximal, i.e. it can not be extended on
# either side. So as an example, if the character string is “He came, he see, he conquered”, then the
# words are “He”, “came,”, “he”, ”see,”, “he”, “conquered”. Notice that for simplicity we are
# treating
# punctuation marks also as part of words. Also, note that two words may be separated by several
# spaces, not necessarily just one. Finally, we may have spaces also at the beginning or the end of
# the string.
# Write a program to count the number of words in the inputted string.
def count(string):
    c=0  #counter
    li = list(string.split(" "))
    print("The string:",li)
    for i in li:
        c+=1
    return c

str1 = "He came, he see, he conquered"
a = count(str1)
print("The number of words are:",a)
