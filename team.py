from random import randint
from characters import *

def rand_alive(team):
  n = len(team)
  r = randint(0,n-1)
  return r if team[r].alive else rand_alive(team)

def rand_death(team):
  n = len(team)
  r = randint(0,n-1)
  return r if not team[r].alive else rand_death(team) 

def count_alive(team):
  res = 0
  for i in team:
    if i.alive:
      res += 1
  return res

def count_dead(team):
  res = 0
  for i in team:
    if not i.alive:
      res += 1
  return res

def all_dead(team):
  for i in team:
    if i.alive:
      return False
  return True

def all_alive(team):
  for i in team:
    if not i.alive:
      return False
  return True


LONGEST_NAME = 11

def print_stat(team):
  
  if team == []:
    print("(Currently no member in the team now)")
    return
  names = 'Members:   '
  hp =  'Hitpoints: '
  sth  =  'Strength:  '
  maxm =  'Max. Mana: '
  mana =  'Currnet M: '
  for i in team:
    nspace = LONGEST_NAME - len(i.name)
    names += '|' + ' '*nspace   +i.name
    nspace = LONGEST_NAME - len(str(i.hp))
    hp += '|' + ' '*nspace  + str(i.hp)
    if i.str:
      nspace = LONGEST_NAME - len(str(i.str))
      sth += '|' + ' '*nspace  + str(i.str)
    else:
      sth += '|' + ' '*LONGEST_NAME
    if i.maxmana:
      nspace = LONGEST_NAME - len(str(i.maxmana))
      maxm += '|' + ' '*nspace  + str(i.maxmana)
    else:
      maxm += '|' + ' '*LONGEST_NAME
      
    if i.mana:
      nspace = LONGEST_NAME - len(str(i.mana))
      mana += '|' + ' '*nspace  + str(i.mana)
    else:
      mana += '|' + ' '*LONGEST_NAME      
  print(names)
  print(hp)
  print(sth)
  print(maxm)
  print(mana)