from random import randint
from data import letters_grid


num_list = list(range(1,11))

def print_grid():
    grid = [['~'] * 10] * 10
    rows = []
    
    header = ''.join([f'{num:>4}' for num in num_list])
    separators = ''.join([f'{"-":>4}' for _ in range(1, 11)])
    
    rows.append(header)
    rows.append(separators)
    
    for i in range(10):
        first = f'{letters_grid[i+1]}|'
        second = ' '.join(f'{x:3}' for x in grid[i])
        rows.append(first + " " + second)
    return '\n'.join(rows)

def side_by_side():
    user_board = print_grid().split('\n')
    computer_board = print_grid().split('\n')

    width = max(len(row) for row in user_board)

    for r1, r2 in zip(user_board, computer_board):
        print(f'{r1:<{width}}   {r2}')

def get_user_grid():
    pass
def get_computer_grid():
    pass
