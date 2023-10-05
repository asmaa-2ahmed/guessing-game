# Guessing Game Project

This is a simple guessing game implemented in Python. The game generates a random number based on the chosen difficulty level, and the player needs to guess the number within a certain number of trials.

## Getting Started
To play the game, follow these steps:
1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Open the Project 1: Guessing Game.ipynb file in a Python environment or Jupyter Notebook.

## Game Levels

1. Easy:
   - Limits: 1 to 10
   - Number of trials: 3

2. Intermediate:
   - Limits: 1 to 100
   - Number of trials: 7

3. Hard:
   - Limits: 1 to 1000
   - Number of trials: 15

## Solution Overview

The solution can be divided into several parts:

1. Showing the game levels to the player.
2. Asking the player to choose the game level.
3. Setting the game settings based on the chosen level.
4. Starting the game and allowing the player to make guesses.
5. Providing feedback to the player based on their guesses.
6. Ending the game and displaying the result.

## Solution Implementation

The code provided in the notebook follows the outlined solution. Here is a brief overview of the implemented functions:

1. `show_levels()`: This function displays the available game levels to the player.

2. `game_level_choice()`: This function asks the player to choose a game level and returns the selected level.

3. `set_game_settings(game_level)`: This function sets the game settings (limits and number of trials) based on the chosen game level.

4. `start_play(limits, n_trials)`: This function starts the game and allows the player to make guesses. It compares the player's guess with the randomly generated number and provides feedback on whether the guess should be increased or decreased. The game continues until the player guesses the correct number or runs out of trials.

5. `play()`: This function orchestrates the entire game by calling the previous functions in the appropriate order.

## How to Play

1. Run the code provided in the notebook.

2. The game levels will be displayed.

3. Choose a game level by entering the corresponding number.

4. The game will set the number range and the number of trials based on the chosen level.

5. Start guessing the number within the given trials.

6. Based on your guess, the game will provide feedback on whether you should increase or decrease your guess.

7. Keep making guesses until you guess the correct number or run out of trials.

8. The game will display the result: either a congratulations message with the number of trials it took you to guess correctly, or a "You Lose!" message with the correct number.

9. You can play the game again by re-running the code.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## Acknowledgments
This project is a simple implementation of a guessing game and is meant for educational purposes. Feel free to modify and improve it as needed.

Enjoy playing the game!
