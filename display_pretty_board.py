from data import letters_grid


# This fucntion is aimed to display the user and computer board side by side.
# The function should print the column letters, A-J and the numbers on the rows, 1-10.
# The output should be a random column and row. 

test_board = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', 'X', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', 'X', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', 'X', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

def display_pretty_board(board):

    for _ in enumerate(board):
        for i in _:
            print(i, end= " ")
        print()

display_pretty_board(test_board)
        




