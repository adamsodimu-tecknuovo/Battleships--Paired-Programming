# This module will print the ship as X on the user and the computer board 
from createship import computer_ship
from create_grid_3 import get_computer_grid, get_user_grid

# This function will take the generated coordinates, 
# and swich the current value of the cell which is ~ by X 
def print_boat():
    grid = get_computer_grid()
    print(f"This is the user GRID:{grid}")
print_boat()