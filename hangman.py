import random

player1_option = input('Do you want player 2 to type the word?')
options_list = ["python", "hangman", "coding", "apprentice", "project"]

word_list = []
hidden_word = []
correct_letters = []
track_the_letter = []
player1 = None
player2 = None


if player1_option == 'yes':
    word_to_guess = input("Choose a word of your preference: ")
else:
    word_to_guess = random.choice(options_list)

for i in range(len(word_to_guess)):
    word_list.append(word_to_guess[i])
for i in range(len(word_list)):
    hidden_word.append('_')

print(hidden_word)


lives = 6 
while lives:
    # ask user to guess the a letter 
    print(f'Lives remaining : {lives}')
    player_1_guess = input('Guess a letter: ')

    if player_1_guess is int:
         print("Please choose a valid letter")
    if player_1_guess not in track_the_letter:
                track_the_letter.append(player_1_guess)
    if player_1_guess in word_list:
        print ('Correct!')
        for the_index, i in enumerate(word_list):
            if i == player_1_guess:
                hidden_word[the_index] = player_1_guess
                correct_letters.append(i) 
          
        print(hidden_word)
        print(f'Letters you have already guessed: {track_the_letter}')
    else:
        lives -=1 
        print(f'Letters you have already guessed: {track_the_letter}')

    if lives == 0:
        print("You lost!")
        break
    elif len(correct_letters)== len(word_list):
        print("Congratulations you have guess the word! You have won! ")
        break

        
            


    





