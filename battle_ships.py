from random import randint


letters_grid = {
    1 : 'A',
    2 : 'B',
    3 : 'C',
    4 : 'D',
    5 : 'E',
    6 : 'F',
    7 : 'G',
    8 : 'H',
    9 : 'I',
    10 : 'J' 
    }
num_list = list(range(1,11))

def print_grid():
    grid = [['~'] * 10] * 10
    print(''.join([f'{num:>4}' for num in num_list]))
    print(''.join([f'{"_":>4}' for _ in range(1, 11)]))
    for i in range(10):
            print(f'{letters_grid[i+1]}|', end=' ')
            print(' '.join(f'{x:3}' for x in grid[i]))
            

grid_1 = print_grid()
grid_2 = print_grid()

print(grid_1, grid_2)



