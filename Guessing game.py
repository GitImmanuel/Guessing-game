#Guessing game by Immanuel, http://github.com/GitImmanuel, 11-05-2017
#Importing stuff
import math
import sys
import time
import random

print("Press 'Enter' at any input to exit.")
time.sleep(1)

#Welcome
print('Welcome to my guessing game!')
print('')
time.sleep(1)

#Showing modes
print('There are 5 modes: ')
print('- Noob')
print('- Easy')
print('- Normal')
print('- Hard')
print('- Insane')
print('')


def playmore():
    PlayMore = input('Do you want to play more? (y/n): ')
    print('')
    if PlayMore == "y" or PlayMore == "Y" or PlayMore == "yes" or PlayMore == "Yes":
        askmode()
    elif PlayMore == "n" or PlayMore == "no" or PlayMore == "No" or PlayMore == "N":
        print('Thank you for playing with us!')
    else:
        print('Please answer yes or no.')
        playmore()

def noob():
    global found, userGuess
    print('Guess if the number is 1 or 2.')
    randomNumber = random.randint(1, 2)
    found = False

    while not found:

        def lol():
            try:
                global userGuess
                userGuess = int(input("Your guess: "))
            except (SyntaxError, ValueError):
                print('')
                print('Please enter a number.')
                lol()

        lol()

        if userGuess == randomNumber:
            print('')
            print('Congratulations! You have found the number.')
            print('')
            found = True
            playmore()
        elif userGuess < randomNumber:
            print('')
            print('The answer is 2.')
        elif userGuess > randomNumber:
            print('')
            print('The answer is 1.')

def easy():
    global found, userGuess
    print('Guess a number between 1 and 10.')
    randomNumber = random.randint(1,10)
    found = False

    while not found:
        def lol():
            try:
                global userGuess
                userGuess = int(input("Your guess: "))
            except (SyntaxError, ValueError):
                print('')
                print('Please enter a number.')
                lol()

        lol()

        if userGuess == randomNumber:
            print('')
            print("Congratulations! You have found the number.")
            print('')
            found = True
            playmore()
        elif userGuess < randomNumber:
            print('')
            print('Guess higher!')
        elif userGuess > randomNumber:
            print('')
            print('Guess lower!')

def normal():
    global found, userGuess
    print('Guess a number between 1 and 100.')
    randomNumber = random.randint(1, 100)
    found = False

    while not found:
        def lol():
            try:
                global userGuess
                userGuess = int(input("Your guess: "))
            except (SyntaxError, ValueError):
                print('')
                print('Please enter a number.')
                lol()

        lol()

        if userGuess == randomNumber:
            print('')
            print("Congratulations! You have found the number.")
            print('')
            found = True
            playmore()
        elif userGuess < randomNumber:
            print('')
            print('Guess higher!')
        elif userGuess > randomNumber:
            print('')
            print('Guess lower!')

def hard():
    global found, userGuess
    print('Guess a number between 1 and 1000.')
    randomNumber = random.randint(1, 1000)
    found = False

    while not found:
        def lol():
            try:
                global userGuess
                userGuess = int(input("Your guess: "))
            except (SyntaxError, ValueError):
                print('')
                print('Please enter a number.')
                lol()

        lol()
        if userGuess == randomNumber:
            print('')
            print("Congratulations! You have found the number.")
            print('')
            found = True
            playmore()
        elif userGuess < randomNumber:
            print('')
            print('Guess higher!')
        elif userGuess > randomNumber:
            print('')
            print('Guess lower!')

def insane():
    global found, userGuess
    print('Guess a number between 1 and 1000.')
    randomNumber = random.randint(1, 1000)
    found = False

    while not found:
        def lol():
            try:
                global userGuess
                userGuess = int(input("Your guess: "))
            except (SyntaxError, ValueError):
                print('')
                print('Please enter a number.')
                lol()

        lol()

        if userGuess == randomNumber:
            print('')
            print("Congratulations! You have found the number.")
            print('')
            found = True
            playmore()
        else:
            print('')
            print('Guess further')

#Asking mode
def askmode():
    global mode
    mode = input('Choose your mode: ')
    print('')

    def further():
        if mode == "Noob" or mode == "N" or mode == "noob" or mode == "n":
            noob()
        elif mode == "Easy" or mode == "E" or mode == "easy" or mode == "e":
            easy()
        elif mode == "Normal" or mode == "N" or mode == "normal" or mode == "n":
            normal()
        elif mode == "Hard" or mode == "H" or mode == "hard" or mode == "h":
            hard()
        elif mode == "Insane" or mode == "I" or mode == "i" or mode == "insane":
            insane()

    # More checking
    def checkmode2():
        global check
        if check == "y" or check == "yes":
            print("Okay, let's go!")
            print('')
            further()
        elif check == "n" or check == "no":
            print('No worries, we will ask you again!')
            askmode()
        else:
            print('Please answer yes or no.')
            check = input("The mode you chose was '" + str(mode) + "', is that right? (y/n): ")
            checkmode2()

    # Checking
    def checkmode1():
        global check
        if mode == "Noob" or mode == "N" or mode == "noob" or mode == "n":
            print('You have chosen for the noob mode!')
            check = input('Is this right? (y/n): ')
            print('')
            checkmode2()
        elif mode == "Easy" or mode == "E" or mode == "easy" or mode == "e":
            print('You have chosen for the easy mode!')
            check = input('Is this right? (y/n): ')
            print('')
            checkmode2()
        elif mode == "Normal" or mode == "N" or mode == "normal" or mode == "n":
            print('You have chosen the normal mode!')
            check = input('Is this right? (y/n): ')
            print('')
            checkmode2()
        elif mode == "Hard" or mode == "H" or mode == "hard" or mode == "h":
            print('You have chosen the hard mode!')
            check = input('Is this right? (y/n): ')
            print('')
            checkmode2()
        elif mode == "Insane" or mode == "I" or mode == "i" or mode == "insane":
            print('You have chosen for the insane mode!')
            check = input('Is this right? (y/n): ')
            print('')
            checkmode2()
        else:
            print("That's not a mode.")
            askmode()



    checkmode1()

askmode()

input("Press 'Enter' to exit.")

