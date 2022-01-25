
# processing
def Cost_Calculator(cost, area1):
    finalCost = cost * area1
    # output
    print('It will cost ', '$', finalCost, ' without tax')


# processing
def Area_Calculator(length1, width1):
    area = length1 * width1
    Cost_Calculator(2.25, area)


while True:
    print('do you want to calculate carpenting cost?')
    wantQuit = input()
    if wantQuit.upper() == 'NO':
        break
    elif wantQuit.upper() == 'N':
        break
    else:
        # inputs
        print('length of tile (meters)')
        length = int(input())
        print('width of tile (meters)')
        width = int(input())
        Area_Calculator(length, width)
