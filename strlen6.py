# 7) Python program to calculate length of a string using recursion 
str = input("Enter a string:")
  
def strlen(str) : 
    if str == '': 
        return 0
    else : 
        return 1 + strlen(str[1:])  
      
print ("Number of characters in a string:",strlen(str)) 