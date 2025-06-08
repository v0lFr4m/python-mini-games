import random

def you_win_message():
    return f'\n|==============================================================================|\n                             Computer choose: {computer_says} \n|---------------------------------- YOU WIN -----------------------------------|\n|==============================================================================|\n\n\n\n\n'

def draw_message():
    return f'\n|==============================================================================|\n                             Computer choose: {computer_says} \n|------------------------------ THE GAME IS DRAW ------------------------------|\n|==============================================================================|\n\n'

def you_lose_message():
    return f'\n|==============================================================================|\n                             Computer choose: {computer_says} \n|--------------------------------- YOU LOSE -----------------------------------|\n|==============================================================================|\n\n'

def greeting():
    return '|==============================================================================|\n|------------------- Welcome to game Rock , Paper , Scissors ------------------|\n|==============================================================================|\n|---------------------------- The rules are simple, ---------------------------|\n|-------------- You need to enter Rock ,Paper , Scissors ----------------------|\n|==============================================================================|\n'

def final_score(player_score :int ,computer_score: int , player_games : int):
       return f'|==============================================================================|\n                             Player score: {player_score} \n                             Player score: {computer_score} \n                             Games played: {player_games} \n|==============================================================================|\n'



def you_win(player :str , computer :str):
    if  (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        return True

def is_draw(player :str , computer :str):
    if player == computer:
        return True

computer_wins = 0
user_wins = 0
game_counter = 0

COMPUTER_OPTIONS = ["rock", "paper", "scissors"]

print(greeting())
while True:
    computer_says = random.choice(COMPUTER_OPTIONS)
    player_move = input("Choose [r]ock , [p]paper , [s]cissors: ").lower()

    if player_move == 'r':
        player_move = 'rock'
    elif player_move == 'p':
        player_move = 'paper'
    elif player_move == 's':
        player_move = 'scissors'
    else:
        print('\nInvalid input! Try again... \n')
        continue

    if you_win(player_move , computer_says):
        user_wins += 1
        game_counter += 1
        print(you_win_message())
        command = input("Do you want to play again YES/NO:").lower()

        if command == 'yes':
            print(greeting())
            continue
            
        elif command == "no":
            print(final_score(user_wins, computer_wins, game_counter))
            break

    elif is_draw(player_move , computer_says):
        game_counter += 1
        print(draw_message())
    else:
        game_counter += 1
        computer_wins += 1
        print(you_lose_message())



    # TODO:
    # SQUID GAME TYPE ROCK PAPER SCISSORS WITH TWO HANDS

