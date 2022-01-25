# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Pythagoras
# DATE OF CREATION:  24/1/2022
# PURPOSE OF PROGRAM:  Calculate Pythagoras theorem
import math


# processing
def Pythagoras(A, B):
    C = (A ^ 2) + (B ^ 2)
    # outputs
    print('Third side =', math.sqrt(C), '\n')


while True:
    print('do you want to calculate Pythagoras Theorum?')
    wantQuit = input()
    if wantQuit.upper() == 'NO':
        break
    elif wantQuit.upper() == 'N':
        break
    else:
        # inputs
        print('base of triangle')
        side1 = int(input())
        print('height of triangle')
        side2 = int(input())
        Pythagoras(side1, side2)
