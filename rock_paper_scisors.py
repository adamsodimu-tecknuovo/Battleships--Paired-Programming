# import random

# rules = {
#     'rock': {'wins': 'sissors', 'loses':'paper'},
#     'paper': {'wins': 'rock', 'loses':'sissors'},
#     'sissors': {'wins': 'paper', 'loses':'rock'}
# }

# def game_output(user_choice, computer_choice):
#     print(f'You:{user_choice}, Computer:{computer_choice}')
#     if user_choice not in rules:
#         return "Input a valid choice"
#         print("123")
#     if rules[user_choice]['wins'] == computer_choice:
#         return 'You Win'
#         print("0123")
#     if rules[user_choice]['loses'] == computer_choice:
#         return 'You Lose'
#         print("12345")
#     if rules[user_choice] == computer_choice:
#         return 'tie'
#         print("12378")

# game_continue = True 
# while game_continue:
    
#     user = input("Choose rock, paper or sissors:")
#     options = ['rock', 'paper', 'sissors']
#     computer = random.choice(options)

#     game = game_output(user, computer)
#     print(game)
  
#     game_cont = input('Do you want to play again?')
#     if game_cont == 'no':
#         game_continue = False


    




# # if computer_choice == user_choice:
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'paper':
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'scisors':
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'rock':
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'rock':
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'rock':
# #     print('Tie, try again')
# # if computer_choice == 'rock' and user_choice == 'rock':
# #     print('Tie, try again')
 

import random

rules = {
    'rock': {'wins': 'sissors', 'loses':'paper'},
    'paper': {'wins': 'rock', 'loses':'sissors'},
    'sissors': {'wins': 'paper', 'loses':'rock'}
}

def game_output(user_choice, computer_choice):
    print(f'You:{user_choice}, Computer:{computer_choice}')

    if user_choice not in rules:
        return "Input a valid choice"
    if user_choice == computer_choice:
        return 'tie'
    if rules[user_choice]['wins'] == computer_choice:
        return 'You Win'
    if rules[user_choice]['loses'] == computer_choice:
        return 'You Lose'

options = ['rock', 'paper', 'sissors']    
computer = random.choice(options)

game_continue = True 
while game_continue:
    
    user = input("Choose rock, paper or sissors:")
    
    
    print(computer)

    game = game_output(user, computer)
    print(game)
  
    game_cont = input('Do you want to play again?')
    if game_cont == 'no':
        game_continue = False


    




# if computer_choice == user_choice:
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'paper':
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'scisors':
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'rock':
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'rock':
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'rock':
#     print('Tie, try again')
# if computer_choice == 'rock' and user_choice == 'rock':
#     print('Tie, try again')
 