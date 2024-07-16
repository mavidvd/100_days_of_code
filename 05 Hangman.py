# def my_function():
#     # do this
#     # do that
#     # all commands are indented

# my_function()       # we have to call the function

# Hangman

from getpass import getpass

solution = getpass("Which word should be guessed? ").upper()
board = "_" * len(solution)
lives = 5
print(board)
print(f"The length is {len(solution)}.")

def win():
    count_ = 0
    for l in board:
        if l == "_":
            count_ += 1
    if count_ == 0:
        print(f"You won! The word was {board}.")
        return True
    else:
        return False

def lose():
    if lives == 0:
        print(f"You lost! The word was {solution}.")
        return True
    else:
        return False
    
while not win() and not lose():
    right_guess = 0
    guess = input("Which letter are you guessing? ").upper()
    for x in range(len(solution)):
        split_board = list(board)
        if solution[x] == guess:
            split_board[x] = guess
            right_guess += 1
        board = ''.join(split_board)
    if right_guess == 0:
        lives -= 1
    print(board)
    print(f"You have {lives} lives remaining.\n")

