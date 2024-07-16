# fruits = ["peach", "apple", "pear"]
# for _ in fruits:
#     print(_)

# nums = [1, 2, 4, 5, 6, 9, 12]
# for x in nums:
#     if x % 2 == 0:
#         print(f"{x} is divisible by 2.")
#     else:
#         print(f"{x} is not divisible by 2.")
#     if x % 3 == 0:
#         print(f"{x} is divisible by 3.")
#     else:
#         print(f"{x} is not divisible by 3.")
#     if x % 5 == 0:
#         print(f"{x} is divisible by 5.")
#     else:
#         print(f"{x} is not divisible by 5.")

# numlist = range(1,6)
# for x in numlist:
#     for y in numlist:
#         print(f"{x} * {y} = {x*y}")
#     print("\n")

# Student Height Exercise. Input a list of heights (cm) and get the Average Height.
# heights = input("Write the list of heights: ").split()
# heightsum = 0
# count = 0
# for x in heights:
#     heightsum += int(x)
#     count += 1
# print(f"The average height of the {count} student(s) is {heightsum/count}cm.")

# Find the highest number in a list exercise.
# numlist = input("Write the list of numbers: ").split()
# maxnum = 0
# for x in numlist:
#     if int(x) > maxnum:
#         maxnum = int(x)
# print(f"The highest number of the list was {maxnum}.")

# Find the sum of numbers 1 to 100 (or any two given numbers).
# total = 0
# minrange = int(input("What's the number you want to start with? "))
# maxrange = int(input("What's the number where you want to stop? "))
# step = int(input("What should be the step value? "))
# for x in range(minrange, maxrange + 1, step):
#     total += x
# print(f"The total sum between {minrange} and {maxrange} is {total}.")

# FizzBuzz exercise. Print numbers from 1 to 100 but if they are divisible by 3, print Fizz, if by 5 then Buzz and if by 15 then FizzBuzz.
# for x in range (1, 101):
#     if x % 15 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)

# Password Generator Project.
import random
letters = ["a", "b", "c", "d", "e", "A", "B", "C", "D", "E"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "*", "@", "%"]
password = []

num_letters = int(input("How many letters do you want the password to have? "))
num_numbers = int(input("How many numbers do you want the password to have? "))
num_symbols = int(input("How many symbols do you want the password to have? "))

for x in range(num_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])
for x in range(num_numbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])
for x in range(num_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])
random.shuffle(password)
print(f"Your password is {''.join(password)}.")
