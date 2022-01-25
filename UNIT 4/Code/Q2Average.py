
# variables
sumnum = 0
total = 0


print('Type "0" to stop adding numbers and get your result')
while True:
    # inputs
    user_input = input()
    if user_input == '0':
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
