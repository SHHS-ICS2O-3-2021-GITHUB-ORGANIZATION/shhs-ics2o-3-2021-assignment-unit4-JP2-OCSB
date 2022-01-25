import random

# processing
def Random_Number_Generator(num1, num2):
    random_number = random.randint(num1, num2)
    # outputs
    print('your number is', random_number)


while True:
    print('do you want to calculate a random number?')
    wantQuit = input()
    if wantQuit.upper() == 'NO':
        break
    elif wantQuit.upper() == 'N':
        break
    else:
        # inputs
        print('You will make a range')
        print('from:')
        number1 = int(input())
        print('to:')
        number2 = int(input())
        Random_Number_Generator(number1, number2)
