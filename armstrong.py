# Python program to find all the armstrong numbers within the given range
lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))

print("The armstrong number in the given range is:")
for num in range(lower, upper + 1):

    order = len(str(num))  # Counting the digits
    sum = 0
    k = num
    while k > 0:
        d = k % 10
        sum += d ** order
        k //= 10
    if num == sum:
        print(num,end=" ")