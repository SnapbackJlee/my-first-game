import random
from tkinter import Y
guesses= 5

while True:
    user_input = input("Press 'Y' if you like poop. and want\n to play a stinky lil game. Press 'Q' to quit..")
    computer_number = random.randint(1,10)

    if user_input == 'Q'.lower():
        break

    elif user_input == 'Y'.lower():
        print("thats disgusting")
    print("I'm thinking of a number between 1 and 10\n you have five try's")
    print("---------------------------------------------")

    while guesses > 0:
    
        user_guess = input(f"What is your guess, you have {guesses} try's left. ")

        if int(user_guess) == computer_number:
            print("YOU ARE CORRECT YOU WIN!")
            break

        else:
            guesses -= 1
            print(f"I'm sorry that is incorrect you have {guesses} left.")
            print("---------------------------------------------")

    break
print(f"the correct number is {computer_number}")
print("GAME OVER GOODBYE")
    
