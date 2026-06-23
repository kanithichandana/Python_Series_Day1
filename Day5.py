# Problem 1: Sum of First N Natural Numbers
def sum_of_natural_nums(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum += i
    return(total_sum)
n=int(input("Enter n number:"))
print(sum_of_natural_nums(n))

# Problem 2: Multiplication Table
def multiply_table(n):
    for i in range(1,11):
        product=n*i
        print(f"{n}*{i}={product}")
n=int(input("Enter n number:"))
print(multiply_table(n))

# Problem 3: Count Digits in a Number
def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n = n // 10 
        count += 1 
    print(count)
n=int(input("Enter n number:"))
print(count_digits(n))

# Problem 4: Reverse a Number
def reverse_number(n):
    reversed_num = 0
    while n> 0:
       last_digit = n % 10 
       reversed_num = (reversed_num * 10) + last_digit
       n = n // 10 
    print(reversed_num)
n=int(input("Enter n number:"))   
print(reverse_number(n)) 

# Problem 5: Check Prime Number
def is_prime(N):
    if N <= 1:
        print("Not Prime")
        return
# Check for factors up to the square root of N
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
N=int(input("Enter N number:"))    
print(is_prime(N))  