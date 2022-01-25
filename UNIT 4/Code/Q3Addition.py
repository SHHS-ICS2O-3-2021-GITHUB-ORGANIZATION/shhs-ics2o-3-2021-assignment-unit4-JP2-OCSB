# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Addition
# DATE OF CREATION:  24/1/2022
# PURPOSE OF PROGRAM:  An addition game
import random


def Game():
    # processing
    A = random.randint(1, 100)
    B = random.randint(1, 100)
    equation_ans = A+B
    print(f'{A} + {B} = ?')
    guess = int(input())
    # outputs
    if guess == equation_ans:
        print('You got it!\n')
        return
    else:
        print('You got it wrong\n')
        return


while True:
    # inputs
    print('do you want to play?')
    ans1 = input()
    if ans1.upper() == 'NO':
        break
    elif ans1.upper() == 'N':
        break
    else:
        Game()
