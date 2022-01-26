# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  questions
# DATE OF CREATION:  26/1/2022
# PURPOSE OF PROGRAM:  makes a question

# variables
file = open('questions', 'a')
file2 = open('answers', 'a')

while True:
    # inputs
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
    # outputs
    file.write(f'{question}\n')
    print('choice A)')
    answerA = input()
    # outputs
    file.write(f'A) {answerA}\n')
    print('choice B)')
    choiceB = input()
    # outputs
    file.write(f'B) {choiceB}\n')
    print('choice C')
    choiceC = input()
    # outputs
    file.write(f'C) {choiceC}\n')
    print('choice D')
    choiceD = input()
    # outputs
    file.write(f'D) {choiceD}\n\n')
    print('what is the right answer?')
    answer = input()
    # outputs
    file2.write(f'{answer}\n')





