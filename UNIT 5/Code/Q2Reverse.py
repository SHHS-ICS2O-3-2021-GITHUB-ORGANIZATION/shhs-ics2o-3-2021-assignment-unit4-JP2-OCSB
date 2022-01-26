# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  reverse
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM: Reverses a string

while True:
    # inputs
    print('do you want to quit')
    userInput = input()
    if userInput.lower() == 'yes':
        break
    elif userInput.lower() == 'y':
        break
    # inputs
    print('type your word')
    word = input()
    # processing/outputs
    for i in range(len(word)):
        print(word[len(word)-1-i])