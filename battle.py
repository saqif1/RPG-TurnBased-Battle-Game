from characters import *
from random import randint
from team import *

# You increase nCharType one at a time 
NUM_CHAR = 2    # no. of types of characters you can choose
GOLD     = 200  # Gold for you to recruit characters
MIN_COST = 100  # A hack for user_choose_team()

'''
Type:
1: Fighter (Given)
2: Mage (Given)
3: Berserker 
4: ArchMage
5: Necromancer
'''

def create_char(i):
  if i == 1:
    return Fighter()
  elif i == 2:
    return Mage()
# UNCOMMENT ONCE YOU HAVE IMPLEMENTED THE NECESSARY CLASS
#   elif i == 3:
#     return Berserker()
#   elif i == 4:
#     return ArchMage()
#   elif i == 5:
#     return Necromancer()


def create_rand_team(gold):
  team = []
  while gold > 0:
    tempChar = create_char(randint(1, NUM_CHAR))
    if gold >= tempChar.cost:
      gold -= tempChar.cost
      team.append(tempChar)     
  return team

def user_choose_team(gold):
  team = []
  choice = -1
  while (gold >= MIN_COST) and (gold != 0) :
    print("\nYour current team:")
    print_stat(team)
    print(f'\nYou have {gold} gold currently')
    choice = -1
    while choice < 1 or choice > NUM_CHAR:
      print("Choices:")
      print(f"1: Fighter (cost: {Fighter().cost})")
      print(f"2: Mage (cost: {Mage().cost})")  
    # UNCOMMENT ONCE YOU HAVE IMPLEMENTED THE NECESSARY CLASS 
    #   print(f"3: Berserker (cost: {Berserker().cost})")
    #   print(f"4: ArchMage (cost: {ArchMage().cost})")
    #   print(f"5: Necromancer (cost: {Necromancer().cost})")
      choice = int(input(f'Input a choice from 1 to {NUM_CHAR}:'))
      if choice < 1 or choice > NUM_CHAR:
        print(f"Your choice {choice} is not valid. Please choose again")
    if choice > 0 and choice <= NUM_CHAR:
      temp_char = create_char(choice)
      if gold >= temp_char.cost:
        gold -= temp_char.cost
        team.append(temp_char)     
  return team

def run_battle(team_a, team_b, pause = True):
  # Return 0 when Team A win and 1 otherwise.
  # There will be no tie

  rd = 0
  a_turn = True
  dprint("")
  dprint("THE BATTLE STARTS!!!!!")

  while (not all_dead(team_a)) and not all_dead(team_b):
    dprint('')
    
    if a_turn:
      attacker_team = team_a
      defender_team = team_b
      rd += 1
      dprint(f'Round {rd}')
    else:
      attacker_team = team_b
      defender_team = team_a

    if DEBUG_PRINT:
      print("Team A:")
      print_stat(team_a)
      print()
      print("Team B:")
      print_stat(team_b)

    dprint('')
    
    attacker = rand_alive(attacker_team)
    team_s = 'Team A' if a_turn else 'Team B'
      
    dprint(team_s + f' member {attacker} {attacker_team[attacker].name} acts')
    attacker_team[attacker].act(attacker_team, defender_team)
    a_turn = not a_turn
    if pause:
      input("Press Enter to continue....")
    
  if all_dead(team_b):
    dprint("First team won!")
    return 0
  else:
    dprint("Second team won!")
    return 1


def game_start(gold,pause = True):
  enemy = create_rand_team(gold)
  print("Your enemy will be:")
  print_stat(enemy)
  my_team = user_choose_team(gold)
  if run_battle(my_team, enemy, pause) == 0:
    print("Congratz! You won!")
  else:
    print("Sorry, you lose")


game_start(GOLD,False) # The second parameter is to wait for each turn