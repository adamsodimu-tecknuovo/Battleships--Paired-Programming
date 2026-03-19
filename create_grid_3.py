from random import randint
from data import letters_grid


num_list = list(range(1,11))

# def generate_grid():
#     grid = [['~'] * 10] * 10
#     rows = []
    
#     header = ''.join([f'{num:>4}' for num in num_list])
#     separators = ''.join([f'{"-":>4}' for _ in range(1, 11)])
    
#     rows.append(header)
#     rows.append(separators)
    
#     for i in range(10):
#         first = f'{letters_grid[i+1]}|'
#         second = ' '.join(f'{x:3}' for x in grid[i])
#         rows.append(first + " " + second)
#     return '\n'.join(rows)

# this function is intended to generate the actual playing board since the funtion 
# initailly created was primarily printing out the visual board for th user and generatinmg the playing board.
# it was doing too much. 
# I'm using list comprehension (research further)
def generate_playing_grid():
    cols, rows = 10, 10
    playing_board = [["~" for i in range (cols)] for j in range (rows)]
    

    print(f"This is the playing board : {playing_board}")


# def store_user_grid():
#     generate_grid()
# def store_computer_grid():
#     generate_grid()

def side_by_side():
    user_board = store_user_grid().split('\n')
    computer_board = store_computer_grid().split('\n')

    width = max(len(row) for row in user_board)

    for r1, r2 in zip(user_board, computer_board):
        print(f'{r1:<{width}}   {r2}')

generate_playing_grid()