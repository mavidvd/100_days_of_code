# height = int(input("What's your height in cm? "))
# age = int(input("How old are you? "))
# if height >= 120:
#     if age < 12:
#         print("You can ride, your price is $5")
#     elif age < 18:
#         print("You can ride, your price is $8")
#     else:
#         print("You can ride, your price is $12")
# else:
#     print("Unfortunately, you cannot ride yet...")

# number = int(input("Write an integer number: "))
# if number % 2 == 0:
#     print("Your number is even.")
# else:
#     print("Your number is odd.")

# year = int(input("Which year are you checking? "))
# if year % 400 == 0:
#     print("Leap year.")
# elif year % 100 == 0:
#     print("Non-Leap year.")
# elif year % 4 == 0:
#     print("Leap year.")
# else:
#     print("Non-Leap year.")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Non-Leap Year.")
#     else:
#         print("Leap Year.")

height = int(input("What's your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    if age < 12:
        price = 5
    elif age < 18:
        price = 8
    else:
        price = 12
    photo = input("Do you want a photo? ")
    if photo == "Yes":
        price += 3
    print(f"Your ticket is ${price}.")        
else:
    print("Unfortunately, you cannot ride yet...")