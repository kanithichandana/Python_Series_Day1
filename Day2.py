# Problem 1: Check whether a number is positive. #
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# Problem 2: Check whether a number is divisible by 5. #
num = int(input("Enter an integer: "))
if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# Problem 3: Check whether a person is eligible to vote (age ≥ 18). #
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Problem 4: Check whether a number is even or odd. #
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Problem 5: Find the larger of two numbers. #
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is larger.")
else:
    print(f"{num2} is larger.")

# Problem 6: Check whether a student has passed or failed (pass marks = 35). #
marks = float(input("Enter student's marks: "))
if marks >= 35:
    print("Result: Passed")
else:
    print("Result: Failed")

# Problem 7: Check whether a number is positive, negative, or zero. #
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Problem 8: Check whether a person is a child, teenager, adult, or senior citizen based on age.#
age = int(input("Enter age: "))
if age < 13:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")

# Problem 9: Find the largest among three numbers. #
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is the largest number.")
elif b >= a and b >= c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

# Problem 10: Store Discount Calculation. #
purchase_amount = float(input("Enter total purchase amount (₹): "))
if purchase_amount > 5000:
    discount = purchase_amount * 0.20
    print("Eligible for a 20% discount!")
else:
    discount = 0.0
final_payable = purchase_amount - discount
print(f"Final amount payable: ₹{final_payable:.2f}")