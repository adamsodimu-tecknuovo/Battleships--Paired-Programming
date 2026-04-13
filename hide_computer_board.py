
def hide_computer_board(board):
    hidden_board = []
    for i in board:
        new_row = []
        for j in i:
            if j =="X":
                new_row.append("~")
            else:
                new_row.append(j)
        hidden_board.append(new_row)
    return hidden_board