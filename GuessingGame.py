# ****************************** SIMPLE GUESSING GAME *********************************************
# INPUT STATEMENT
# WHILE LOOP
# IF STATEMENT

secred_word = "laptop"

user_guess = input("Enter a word: ")

while user_guess != secred_word:
    user_guess = input("Wrong guess! Please enter a word: ")

print("You have won!")
