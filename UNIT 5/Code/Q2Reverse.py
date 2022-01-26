
while True:
    print('do you want to quit')
    userInput = input()
    if userInput.lower() == 'yes':
        break
    elif userInput.lower() == 'y':
        break
    print('type your word')
    word = input()
    for i in range(len(word)):
        print(word[len(word)-1-i])