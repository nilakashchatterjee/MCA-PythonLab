# 2) Python function that takes a sentence as an input parameter and displays the number of words in the sentence. Python program to count the number of words in a sentence  
def count(string):

    print ("The original string is : " +  string) 
  
    # to count words in string 
    r = len(string.split()) 
  
    return r

string = "This is a python programming assignment"
print ("The number of words are : " +  str(count(string)))