import random 
# # For random integers in a range.
# print(random.randint(1, 10))
# # For random floats.
# print(random.random())
 
# Rock Paper Scissors
comp_random = random.randint(1, 3)
if comp_random == 1:
    comp_choice = "Rock"
elif comp_random == 2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"

your_option = input("Choose R for Rock, P for Paper or S for Scissors. ")
if your_option == "R":
    your_choice = "Rock"
elif your_option == "P":
    your_choice = "Paper"
elif your_option == "S":
    your_choice = "Scissors"
else:
    print("You didn't choose properly.")

if comp_choice == your_choice:
    print(f"The Computer chose {comp_choice} and you also chose {your_choice}; it's a DRAW!")
elif (comp_choice == "Rock" and your_choice == "Paper") | (comp_choice == "Paper" and your_choice == "Scissors") | (comp_choice == "Scissors" and your_choice == "Rock"):
    print(f"The Computer chose {comp_choice} and you chose {your_choice}; YOU WIN!")
elif (comp_choice == "Rock" and your_choice == "Scissors") | (comp_choice == "Paper" and your_choice == "Rock") | (comp_choice == "Scissors" and your_choice == "Paper"):
    print(f"The Computer chose {comp_choice} and you chose {your_choice}; YOU LOSE!")