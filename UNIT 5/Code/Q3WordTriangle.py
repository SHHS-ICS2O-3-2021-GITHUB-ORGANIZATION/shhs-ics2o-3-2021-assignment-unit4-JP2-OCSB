# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Word Triangle
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM:  makes a word triangle

while True:
    print('type your word')
    userInput = input()
    for i in range(1, len(userInput)):
        thing = userInput.split(userInput[i])
        print(thing[0])
        if i == len(userInput)-1:
            print(userInput)



