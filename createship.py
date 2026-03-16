import random
from random import randint
from data import letters_grid

user_ship = []
computer_ship = []


def create_ship(board):

    options = [ 'Horizontal', 'Vertical']

    position = random.choice(options)
    if position == 'Horizontal':
        x = randint(0,10)
        y = randint(0,10)

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





