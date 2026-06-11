# Problem 1: Check whether a number is divisible by both 3 and 5. #
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")

# Problem 2: Check whether an ATM withdrawal can be processed based on available balance and withdrawal amount. #
available_balance = 5000
withdrawal_amount = float(input("Enter withdrawal amount: "))
if withdrawal_amount <= available_balance:
    available_balance -= withdrawal_amount
    print("Withdrawal successful! Remaining balance:", available_balance)
else:
    print("Transaction rejected: Insufficient balance.")

# Problem 3: Check whether a student is eligible for admission if they have either Marks ≥ 70 OR a sports quota certificate. #
marks = int(input("Enter student marks: "))
has_sports_certificate = input("Do you have a sports quota certificate? (yes/no): ").strip().lower() == 'yes'
if marks >= 70 or has_sports_certificate:
    print("Eligible for admission.")
else:
    print("Not eligible for admission.")

# Problem 4: Determine whether a year is a leap year. #
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

