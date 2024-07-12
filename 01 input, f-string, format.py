# city = input("What's the name of the city you grew up in? ")
# pet = input("What was the name of your first pet? ")
# print(f"Your band name will be {city} {pet}!")

# num_char = str(len(input("What is your name? ")))
# print(f"Your name has {num_char} characters.")

# print(type(6/3))
# print(type(6//3))

# height = float(input("Height: "))
# weight = int(input("Weight: "))
# print(f"Your BMI is {weight / height ** 2}")

bill = float(input("How much was the bill? "))
tip = int(input("How much tip (%) do you wanna give? "))
pax = int(input("How many people are splitting? "))
print(f"Each person should pay {bill * (1 + tip / 100) / pax:.2f}€.")