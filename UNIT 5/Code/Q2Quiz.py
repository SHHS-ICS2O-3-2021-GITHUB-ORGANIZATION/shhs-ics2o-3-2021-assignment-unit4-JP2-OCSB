
file = open('questions', 'r')
file2 = open('answers', 'r')

questions = file.read().split('\n\n')
answers = file2.read().split('\n')

score = 0

while True:
    print('do you want to take the quiz?')
    userInput = input()
    if userInput.lower() == 'no':
        break
    elif userInput.lower() == 'n':
        break
    for i in range(len(questions)-1):
        print(questions[i])
        guess = input()
        if guess == answers[i]:
            score = score + 1
    print(f'you got {score} questions out of {len(questions)-1} right!')
