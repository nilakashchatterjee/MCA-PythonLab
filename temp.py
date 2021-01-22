#this program is to convert temperature from fahrenheit to celsius
temp = float(input("Enter the temperature in fahrenheit: "))
print(f"Entered temperature: {temp}ºF")
cel = (temp-32)*(5/9) #coversion of fahrenheit to celsius

print("The temperature in celsius is %0.1fºC " %cel)