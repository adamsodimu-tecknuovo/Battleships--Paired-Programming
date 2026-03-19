import random
from random import randint

user_ship = []
computer_ship = []


def create_ship():

    options = [ 'Horizontal', 'Vertical']

    position = random.choice(options)
    if position == 'Horizontal':
        # We had a rage of 0-10 but I've changed this to 7 
        # since the opeation below (x+1,y) will crash if out of range
        x = randint(0,7)
        y = randint(0,7)

        coordinate = [ (x+i,y) for i in range(3) ]

    else:
        x = randint(0,10)
        y = randint(0,10)

        coordinate = [ (x, y+i) for i in range(3) ]

    return coordinate

        


    # for ship in range(3):
    #     ship_row, ship_column = randint (0,10), (0,10)
    #     while board[ship_row, ship_column] == 'X':
    #         ship_row, ship_column = randint (0,10), randint (0,10)
    #     board[ship_row,ship_column] = 'X'





