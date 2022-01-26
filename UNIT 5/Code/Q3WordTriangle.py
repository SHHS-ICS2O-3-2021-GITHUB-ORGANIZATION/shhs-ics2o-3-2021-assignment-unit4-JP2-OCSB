
while True:
    print('type your word')
    userInput = input()
    for i in range(1, len(userInput)):
        thing = userInput.split(userInput[i])
        print(thing[0])
        if i == len(userInput)-1:
            print(userInput)



