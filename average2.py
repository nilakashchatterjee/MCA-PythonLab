#In this program we are going to aggregate the marks of four subject and print it
sub1 = float(input("Enter the marks of 1st subject: ")) #marks of subject 1
sub2 = float(input("Enter the marks of 2nd subject: ")) #marks of subject 2
sub3 = float(input("Enter the marks of 3rd subject: ")) #marks of subject 3
sub4 = float(input("Enter the marks of 4th subject: ")) #marks of subject 4
sub5 = float(input("Enter the marks of 5th subject: ")) #marks of subject 5

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 4 #aggregate operation of four subjects

if avg<40:
    print(f"Your grade is {avg} \nSorry you're failed....")
else:
    print(f"Your grade is {avg} \nCongratulations you're passed....")