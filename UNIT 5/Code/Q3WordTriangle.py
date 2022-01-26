# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Word Triangle
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM:  makes a word triangle

while True:
    # inputs
    print('type your word')
    userInput = input()
    # processing
    for i in range(1, len(userInput)):
        thing = userInput.split(userInput[i])
        # outputs
        print(thing[0])
        if i == len(userInput)-1:
            print(userInput)



