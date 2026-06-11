# Problem 1: Write a program to print - 'Let’s start the challenge, I will stay consistent'#
print("Let's start the challenge, I will stay consistent")

# Problem 2: Take your name as input and print a welcome message. #
name=input("Enter your name:")
print("Welcome",name ,"Hello! Glad to meet you.")

# Problem 3: Take two numbers as input and print their sum. #
a=int(input("Enter a num:"))
b=int(input("enter b num:"))
print("sum is:",a+b)

# Problem 4: Take two numbers as input and print their Remainder. #
a=int(input("Enter a num:"))
b=int(input("Enter b num:"))
print("Remainder is:",a%b)

# Problem 5: Take three numbers as input and calculate their average. #
a=float(input("Enter a num:"))
b=float(input("Enter b num:"))
c=float(input("Enter c num:"))
d=(a+b+c)/3
print("average is:",d)

#Problem 6: Take two numbers as input and swap their values. #
a=float(input("Enter a num:"))
b=float(input("Enter b num:"))
a,b=b,a
print("Ater swaping:",a)
print("after swaping",b)

# Problem 7: Take marks of 5 subjects as input and calculate the total marks and percentage.#
sub1=float(input("enter sub marks:"))
sub2=float(input("enter sub marks:"))
sub3=float(input("enter sub marks:"))
sub4=float(input("enter sub marks:"))
sub5=float(input("enter sub marks:"))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("Total Marks:",total)
print("percentage is:",percentage)

# Problem 8: Take a temperature in Celsius and convert it to Fahrenheit. #
cel=float(input("Enter temp in celsius:"))
fahr=(cel*9/5)+32
print(cel,"°C translates to",fahr,"°F")

# Problem 9: Take a temperature in Fahrenheit and convert it to Celsius. #
fahr = float(input("Enter temp in fahr:"))
cel=(fahr-3.2)*5/9
print(fahr,"°F translates to" ,cel,"°C")

# Problem 10: Take the length, breadth, and height of a cuboid as input and calculate its volume. #
l= float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
h=float(input("Enter Heigth:"))
volume=l*b*h
print("Volume is:",volume)