# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Counting
# DATE OF CREATION:  25/1/2022
# PURPOSE OF PROGRAM:  Counts

# variables
number = 0

while True:
    print('Enter a value to count down and up to:')
    while True:
        # inputs
        user_input = input()
        try:
            # processing/outputs
            val = int(user_input)
            for i in range(val):
                number = number + 1
                print(number)
            for i in range(val-1):
                number = number - 1
                print(number)

        except ValueError:
            print('not a valid number, try again')
