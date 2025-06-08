import random

# greetings
print('|==============================================================================|')
print('|--------------------- Welcome to game Guess the number -----------------------|')
print('|==============================================================================|')
print('|---------- The rules are simple, you need to enter number --------------------|')
print('|--------------- and the computer will give you a hint ------------------------|')
print('|==============================================================================|')

computer_number = random.randint(1, 100)
current_points = 0

while True:
    player_input = input('Guess the number (1 - 100): ') # player input!
    if not player_input.isdigit():  # check if the number is valid
        print('|==============================================================================|')
        print('|--------------- You need to enter valid number, Try again... -----------------|')
        print('|==============================================================================|')
        continue
    player_number = int(player_input)
    if player_number < 0 or player_number > 100: # check if the number is in range
        print('|----------- You must enter number in range 1 - 100, Try again... -------------|')
        continue

    if player_number == computer_number: # When number is guessed
        print()
        print('|==============================================================================|')
        print('|------------------------- You Guessed the number!-----------------------------|')
        print('|----------------------- Do you want to play again ? --------------------------|')
        print('|-------------------------------- YES / NO ------------------------------------|')
        print('|==============================================================================|')
        print()
        current_points += 10
        player_input = input('You choose : ').lower()
        print()
        if player_input == 'yes':
            computer_number = random.randint(1, 100)  # Computer choose new number
            continue
        else:  # Printing total points
            print ('|==============================================================================|')
            print(f'|-------------------- TOTAL POINTS : {current_points} ---------------------------------------|')
            print ('|==============================================================================|')
            break
    elif player_number < computer_number: # Computer gives hints
        print('|------------------------- The number is too low ! ----------------------------|')
    else:
        print('|------------------------- The number is too high ! ---------------------------|')