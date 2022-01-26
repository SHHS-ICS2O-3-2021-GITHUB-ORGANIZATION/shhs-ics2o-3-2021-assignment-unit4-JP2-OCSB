# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  questions
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM:  makes a question

file = open('questions', 'a')
file2 = open('answers', 'a')

while True:
    print('do you want to add a question?')
    userInput = input()
    if userInput.lower() == 'no':
        break
        file.close()

    elif userInput.lower() == 'n':
        break
        file.close()

    print('what is you question?')
    question = input()
    file.write(f'{question}\n')
    print('choice A)')
    answerA = input()
    file.write(f'A) {answerA}\n')
    print('choice B)')
    choiceB = input()
    file.write(f'B) {choiceB}\n')
    print('choice C')
    choiceC = input()
    file.write(f'C) {choiceC}\n')
    print('choice D')
    choiceD = input()
    file.write(f'D) {choiceD}\n\n')
    print('what is the right answer?')
    answer = input()
    file2.write(f'{answer}\n')





