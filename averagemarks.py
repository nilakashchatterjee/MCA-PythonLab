#In this program we will aggregate the marks of five subject and print the grade
sub1 = float(input("Enter the marks of 1st subject: ")) #marks of subject 1
sub2 = float(input("Enter the marks of 2nd subject: ")) #marks of subject 2
sub3 = float(input("Enter the marks of 3rd subject: ")) #marks of subject 3
sub4 = float(input("Enter the marks of 4th subject: ")) #marks of subject 4
sub5 = float(input("Enter the marks of 5th subject: ")) #marks of subject 5

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5 #aggregate operation of five subjects

# assigning grades
if(avg>=90):
    print("Grade: O")
elif(avg>=80 and avg<90):
    print("Grade: E")
elif(avg>=70 and avg<80):
    print("Grade: A")
else:
    print("Grade: B")
