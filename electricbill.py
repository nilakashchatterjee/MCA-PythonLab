# Here we will input consumed unit and calculate electricity bill
unit = float(input("Enter your consumed unit:"))
if unit <= 300:
    cal = unit * 7
    if cal < 300:
        bill = 300
        print("Your bill is",bill)
    else:
        bill = cal
        print("Your bill is",bill)
elif unit >= 301 and unit <= 800:
    cal = 300*7 + (unit-300)*9
    bill = cal
    print("Your bill is",bill)
elif unit>=801 and unit <= 1500:
    cal = 300*7 + ((unit-300) - (unit - 800))*9 + (unit-800)*12
    bill = cal
    print("Your bill is",bill)
else:
    cal = 300*7 + ((unit-300)- (unit-800))*9 + ((unit-800) - (unit-1500))*12 + (unit-1500)*15
    bill = cal
    print("Your bill is",bill)