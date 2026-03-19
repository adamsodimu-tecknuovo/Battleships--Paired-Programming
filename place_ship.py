# Place ship

# trial_list = [(3, 5), (3, 6), (3, 7)]

# This function should take the coordinates, find the matching position on the board and change the value in the cell.

def place_ship_on_board(coordinates, grid):
    for x,y in coordinates:
        grid[x][y] = "X"
