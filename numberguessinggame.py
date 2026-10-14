# make sure to have the output bar open so you can type in inputs!!!
# yes i coded this with 0 ai help (except for using google to find out about try:)

import random
# just change lives here as you wish this is the only value you should change if you want to
lives = 5
secret_number = random.randint(1, 100) 
# --------------------------------^^^
# you can TECHNICALLY change the second argument here too (whcih i arrowed out)
# but i didn't deal with edge cases of anything other than  over 100 or lesser than 1 so watch yourself
# if you do change it, make sure its not lower than 0 or above 100
guessed = False
def validate_guess(n):
    try:int(n)
    except:
        print(f"The input, {n} must be an integer, for example: 57")
        return False
    number = int(n)
    # If you did change the secret number thing, and want it over a 100 or below 1 change the following here
    #-----------VVV-------------V
    if number > 100 or number < 1:
        # also change this if you wish but its optional
        print(f"The input, {number} must be between 1-100!")
        return False
    else:
         return True
# now the rest of the code is just the actual game itself
while lives > 0 and guessed == False:
    print("Now type a number!")
    inputted_number = input()
    validate = validate_guess(inputted_number)
    if validate:
        print(f"You guessed {inputted_number}")
        if int(inputted_number) != secret_number:
            lives = lives - 1
            print("Wrong guess, Try again!")
            print(f"Lives left: {lives}")
        else:
            print(f"You got the number! It was indeed {secret_number}, and you did it with {lives} lives left!")
            guessed = True
    else:
        print(f"Your guess is invalid for the reason stated above, try again. You still have {lives} left")    
if guessed == False:
    print("You lost! You're now getting mutilated to death by a sharpness 15 tree.")
else:
    print("You're truly the greatest gamer of all time!")
    print("UNLESS IF THE STARTING LIVES WAS ABOVE 10 THEN YOU ARE A COWARD")
    print("if not, congratulations!")
        

    