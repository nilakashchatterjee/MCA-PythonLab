#here we will distinguish between vowel and consonant
char = input("Enter a character: ") #taking user input

if(char=='A' or char=='a' or char=='E' or char =='e' or char=='I'
 or char=='i' or char=='O' or char=='o' or char=='U' or char=='u'):
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")
