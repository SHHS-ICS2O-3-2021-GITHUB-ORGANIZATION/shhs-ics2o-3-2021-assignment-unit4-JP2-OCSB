# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Taxes
# DATE OF CREATION:  25/1/2022
# PURPOSE OF PROGRAM:  Calculates cost with taxes

# variables
taxRate = 13
subtotal = 0.0


while True:
    print('do you want to calculate taxes?')
    wantQuit = input()
    if wantQuit.upper() == 'NO':
        break
    elif wantQuit.upper() == 'N':
        break
    else:
        print('Type stop when you are done adding items')
        while True:
            # inputs
            print('Price of item:')
            user_input = input()
            if user_input.upper() == 'STOP':
                break
            try:
                val = int(user_input)
                subtotal = subtotal + val
            except ValueError:
                try:
                    val1 = float(user_input)
                    subtotal = subtotal + val1
                except ValueError:
                    print('not a number')
        # processing
        tax = subtotal*(taxRate/100)

        # outputs
        print(f'Total cost: ${tax+subtotal}\nTax: ${tax}\nSubtotal: ${subtotal}')
