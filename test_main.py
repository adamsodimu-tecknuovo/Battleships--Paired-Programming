from grid_generator import generate_playing_grid
from createship import create_ship
from place_ship import place_ship_on_board


# This function will be used to link all the 3 modules we created together.
# The first module was the grid generator, which displays the user's board and computer's board.
# The secomd module was the creation of the ship, which generates random numbers,coordinates, from 1-7, due to the later function which adds 1 to the random orientation, horizontal or vertical.
# The third module was the placement of the ship. This is where the random coordinates are placed onto the user and computer's board.

def test_main():
    user_board = generate_playing_grid()
    computer_board = generate_playing_grid()
    user_ship = create_ship()
    computer_ship = create_ship()
    place_ship_on_board(user_ship, user_board)
    place_ship_on_board(computer_ship,computer_board) 
    print(user_board)
    print(computer_board)

test_main()






