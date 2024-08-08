import random  # To generating random choices
import os  # To clear the screen


def select_computer_action():
    """
        Selects a random action for the computer (rock, paper, or scissors).

        Returns:
            str: The computer's chosen action.
    """
    choices = ['rock', 'paper', 'scissors']
    choice = random.choice(choices)
    return choice


def rock_paper_scissors(p_player_choice, p_computer_choice):
    """
        Determines the winner of a rock-paper-scissors round.

        Args:
            p_player_choice (str): The player's choice (rock, paper, or scissors).
            p_computer_choice (str): The computer's choice (rock, paper, or scissors).
    """
    if p_player_choice[0] == p_computer_choice[0]:
        print(f"Both players selected {p_player_choice}. It's a tie!")
    elif p_player_choice == 'rock' or p_player_choice == 'r':
        if p_computer_choice == 'paper' or p_computer_choice == 'p':
            print("Paper covers rock! You lose.")
        elif p_computer_choice == 'scissors' or p_computer_choice == 's':
            print("Rock smashes scissors! You win!")
    elif p_player_choice == 'paper' or p_player_choice == 'p':
        if p_computer_choice == 'rock' or p_computer_choice == 'r':
            print("Paper covers rock! You win!")
        elif p_computer_choice == 'scissors' or p_computer_choice == 's':
            print("Scissors cuts paper! You lose.")
    elif p_player_choice == 'scissors' or p_player_choice == 's':
        if p_computer_choice == 'rock' or p_computer_choice == 'r':
            print("Rock smashes scissors! You lose.")
        elif p_computer_choice == 'paper' or p_computer_choice == 'p':
            print("Scissors cuts paper! You win!")


print("rock, paper, scissors game:")
while True:
    player_choice = input("\nEnter a choice (rock(R), paper(P), scissors(S)): ").lower()
    computer_choice = select_computer_action()
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")
    rock_paper_scissors(player_choice, computer_choice)
    play_again = input("\nPlay again (Y/N)? ").lower()
    if play_again == 'n':
        break
    os.system('cls')  # Clear the screen for a new game

print("End game :)")