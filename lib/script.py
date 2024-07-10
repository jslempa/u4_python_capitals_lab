from capitals import states
import random

def run_game():

    total_correct = 0
    total_incorrect = 0

    random.shuffle(states)

    print('Welcome!')

    for state in states:

        guess = input(f"What is the capital of {state['name']}? ")

        if guess == state['capital']:
            print('Correct')
            total_correct += 1
        else:
            print('Incorrect')
            total_incorrect += 1 

        print(f'\nCorrect: {total_correct}')     
        print(f'Incorrect: {total_incorrect}\n')  

def check_play_again():
    
    play_again = input('Would you like to play again? (Y/N) ')

    if play_again == 'Y':
        run_game()
    else:
        print('Thanks for playing!') 

run_game()   
check_play_again()



