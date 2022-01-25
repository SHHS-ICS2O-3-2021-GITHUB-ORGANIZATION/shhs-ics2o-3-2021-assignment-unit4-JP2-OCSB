
# variables
sumnum = 0
total = 0


while True:
    # inputs
    print('do you want to calculate the average?')
    ans1 = input()
    if ans1.upper() == 'NO':
        break
    elif ans1.upper() == 'N':
        break
    else:
        sumnum = 0
        total = 0
        print('Type "stop" to stop adding numbers and get your result')
        while True:
            # inputs
            print('add a number:')
            user_input = input()
            if user_input.upper() == 'STOP':
                break
            try:
                val = int(user_input)
                sumnum = sumnum + val
                total = total + 1
            except ValueError:
                try:
                    val1 = float(user_input)
                    sumnum = sumnum + val1
                    total = total + 1
                except ValueError:
                    print('not a number try again')
        # outputs/processing
        print(f'the average is: {sumnum/total}')