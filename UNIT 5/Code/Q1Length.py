# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Length
# DATE OF CREATION:  24/1/2022
# PURPOSE OF PROGRAM:  Displays length of a string


while True:
    # inputs
    print('type a word')
    userInput = input()
    # processing/outputs
    print(len(userInput))
    print('do you wanna quit?')
    doquit = input()
    if doquit.upper() == 'YES':
        break
    elif doquit.upper() == 'Y':
        break
