"""
The intent of this file is to create a code to play the game rock, paper, scissors.
The specs are simple, should be a multiplayer game, and the winner would be determined 
by this rules:

Rock beats scissors.
Scissors beat paper.
Paper beats rock.
"""

import random

def play_round(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        return 'win'
    else:
        print("Computer wins!")
        return 'lose'

def main():
    player_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors")
        print("Enter your choice: rock, paper, or scissors. To quit, type 'quit'.")

        player_choice = input("> ").lower()

        if player_choice in ['rock', 'paper', 'scissors']:
            result = play_round(player_choice)
            # Update player's score based on the result
            if result == 'win':
                player_score += 1
            else: 
                computer_score += 1
        elif player_choice == 'quit':
            break
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

    print(f"Final player score: {player_score}, Final cromputer score: {computer_score}")

if __name__ == "__main__":
    main()