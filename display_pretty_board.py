from data import letters_grid


# This fucntion is aimed to display the user and computer board side by side.
# The function should print the column letters, A-J and the numbers on the rows, 1-10.
# The output should be a random column and row. 


def display_pretty_board(board):


    board_builder = []


    # print numbers
    numbers_list = [str(i) for i in range(1,11)]
    numbers = "   " + "  ".join(numbers_list)
    # print(numbers)
    
    for index, row in enumerate(board):
        letter = letters_grid[index+1]
        each_row = " "+"  ".join(row)
        # print(letter, each_row)

    board_builder.append(numbers)
    board_builder.append(letter)
    board_builder.append(each_row)
    print(board_builder)

    



