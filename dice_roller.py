import time
import sys

def delay_print(s):
    #function slows down the text like a gameboy
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
# title
delay_print("Welcome to Lucky Seven \n")
# Number of Players
number_of_players = int(input('How many players are playing?  '))
players = list(range(1, number_of_players+1))
#rules
delay_print("The rules are simple: \n The first player throws the dice. \n If they roll a 7, the player to the right of the roller takes a shot. \n If the roll is not 7, then the roller passes the dice to the left. \n If a player rolls snake eyes everyone takes a shot \n")
#invite
invite = str(input("Are you ready to play? Yes/No "))

#Dice Roll
def turn():
  import random
  die_size = 6
  dice_sum = 0

  for i in range(0,2):
    roll = random.randint(1,die_size)
    dice_sum += roll
    delay_print(f'You rolled a {roll}\n')
  if dice_sum == 2:
    delay_print(f'SNAKE EYES !!!EVERYBODY TAKES A SHOT!!!\n')
  elif dice_sum == 7:
    delay_print(f'Lucky Seven\n')
  else:
    delay_print(f'You have rolled a total of {dice_sum}, Next Player\n')

#Game Play
active= True
while active:
  while players:
    for player in players:
      start = str(input(f'Player {player} are you ready to roll? (Yes/No)\n'))
      if start.lower() == "yes":
        turn()
  else:
    delay_print("Thanks for Playing!, Please Drive Home Safely!")
    active= False
  continue
