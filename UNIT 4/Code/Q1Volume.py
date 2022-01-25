# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Q1Volume
# DATE OF CREATION:  24/1/2022
# PURPOSE OF PROGRAM:  volume of a rectangular prisim

def Volume_Calculator(length, width, depth):
    # processing
    area = int(length) * int(width)
    volume = int(depth) * area
    # outputs
    print('Volume = ', volume, '\n')


while True:
    print('Do you want to quit?')
    wantQuit = input()
    if wantQuit.upper() == 'YES':
        break
    elif wantQuit.upper() == 'Y':
        break
    else:
        # inputs
        print('Define Height')
        height = input()
        print('Define Width')
        width = input()
        print('Define Depth')
        depth = input()
        Volume_Calculator(height, width, depth)
