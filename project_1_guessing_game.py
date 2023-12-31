# -*- coding: utf-8 -*-
"""Project 1: Guessing Game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mfp3JwR2E4jRjUhhpJtkE7F5-tmbTjeI

## Show the game levels
"""

def show_levels():
  print("\nWelcome to the Guessing Game ....... ")
  print("We Have 3 Levels :\n 1- Easy (1-10 and 3 trials)\n 2- Intermediate (1-100 and 7 trials)\n 3- Hard (1-1000 and 15 trials)")

"""## Ask the user for the game level"""

def game_level_choice():
  while True :
    print("**************************************************")
    game_level = int(input("please choose from the menu below :  \n 1- Easy \n 2- Intermediate \n 3- Hard \n"))
    if(game_level in [1,2,3]):
      break
  return game_level

"""## Set the game settings according to the game level:

"""

def set_game_settings(game_level):
  if game_level == 1:
    limits = [i for i in range (11)]
    n_trials=3
  elif game_level == 2:
    limits = [i for i in range (101)]
    n_trials=7
  elif game_level == 3:
    limits = [i for i in range (1001)]
    n_trials=15
  else:
    game_level_choice()
  return limits, n_trials

"""## Start Playing

> Hint: to generate random number in some range:

`import random`

`num = random.randint(lower, upper)`

 or

 `num = random.choice(range(lower, upper))`
"""

import random
def start_play(limits, n_trials):
  num = random.choice(limits)
  choice  = int (input("Let's Start Guessing\t"))
  user_trials=1
  while True :
    #print(f'my choice is {choice}')
    if user_trials < n_trials:
      if choice == num:
        print(f'Congratulations, you achieved it in {user_trials} trial\n the number was {num}')
        break
      else:
        if choice < num :
          print('Increase !!')
        else:
          print('Decrease !!')
        user_trials+=1
        choice=int(input("Another Chance\t"))
    elif user_trials == n_trials and choice != num:
      print(f'You Lose!\n the number was {num} and your choice was {choice}')
      break

"""## Let's Play"""

def play():
  show_levels()
  game_level = game_level_choice()
  limits, n_trials = set_game_settings(game_level)
  start_play(limits, n_trials)

play()