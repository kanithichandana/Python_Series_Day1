# Problem 1: Write a program to print numbers from 1 to 1000
for i in range(1,1001):
    print(i)

# Problem 2: Print the Multiplication Table of a Number
N=int(input("Enter a number:"))
for i in range(1,11):
        print(f"{N}*{i}={N*i}")

# Problem 3: Print All Even Numbers from 1 to N
N=int(input("Enter a number:"))
for i in range(1,N+1):
    if i%2==0:
        print(i)

# Problem 4: Print All Odd Numbers from 1 to N
N=int(input("Enter a number:"))
for i in range(1,N+1):
    if i%2==1:
        print(i)

# Problem 5: Find the Factorial of a Number
N=int(input("Enter a number:"))
factorial=1
for i in range(1,N+1):
    factorial*=i
print(f" The fatorial of {N} is {factorial} ")