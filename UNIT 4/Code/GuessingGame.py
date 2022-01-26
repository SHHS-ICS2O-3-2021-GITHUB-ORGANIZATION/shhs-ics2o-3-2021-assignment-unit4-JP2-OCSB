# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Guessing Game
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM:  A guessing game in python
import random

# variables
number1 = 0
number2 = 0

guesses = 0

randomNumber = 0

# inputs
while True:
    print('do you want to play the guessing game?')
    userInput = input()
    if userInput.upper() == 'NO':
        break
    elif userInput.upper() == 'N':
        break
    else:

        guesses = 0
        while True:
            # inputs
            print('select the smallest number')
            smallnum = input()
            try:
                val = int(smallnum)
                number1 = val
                break
            except ValueError:
                # outputs
                print('not valid try again')

        while True:
            # inputs
            print('select the biggest number')
            bignum = input()
            try:
                val1 = int(bignum)
                number2 = val1
                if number1 >= number2:
                    # outputs
                    print('Bigger number has to be bigger')
                else:
                    break
            except ValueError:
                # outputs
                print('invalid try again')

        # processing
        print(f'Guess between {number1}, and {number2}')
        randomNumber = random.randint(number1, number2)

        while True:
            # processing
            print('your guess is:')
            guess = input()
            guesses = guesses + 1
            try:
                val2 = int(guess)
                if val2 == randomNumber:
                    # outputs
                    print(f'you got it in {guesses} guesses!')
                    break
                else:
                    # outputs
                    print('wrong, try again')
            except ValueError:
                # outputs
                print('not valid number')

