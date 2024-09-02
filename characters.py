from random  import randint
from team import *


### DEBUG PRINT
DEBUG_PRINT = True
def dprint(s):
  if DEBUG_PRINT:
    print(s)

### CONSTANT FOR MAGE
MANA_COST = 20
MANA_RECOVERY = 30


### BASE CHARACTER
class Character():
  def __init__(self):
    self.name = ''
    self.maxhp   = 800
    self.hp      = 800
    self.maxmana = 0
    self.mana    = 0
    self.str     = 0
    self.int     = 0
    self.cost    = 9999999999
    self.alive   = True

  def act(self, my_team, enemy):
    return

  def got_hurt(self, damage):
    if damage >= self.hp:
      self.hp = 0
      self.alive = False
      dprint(self.name + ' died!')
    else:
      self.hp -= damage
      dprint(self.name +
           f' hurt with remaining hp {self.hp}.')

  
### FIGHTER
class Fighter(Character):
  def __init__(self):
    super().__init__()
    self.name  = 'Fighter'
    self.maxhp = 1200
    self.hp    = 1200
    self.str   = 100
    self.cost  = 100

  def act(self, my_team, enemy):
    target = rand_alive(enemy)
    dprint(f'Hurt enemy {target} by damage {self.str}.')
    enemy[target].got_hurt(self.str)

  
### MAGE
class Mage(Character):
  def __init__(self):
    super().__init__()
    self.name    = 'Mage'
    self.maxmana = 50
    self.mana    = 50
    self.cost    = 200
    self.int     = 400

  def cast(self, my_team, enemy):
    self.mana -= MANA_COST
    target = rand_alive(enemy)
    dprint(f'Strike enemy {target} with spell')
    enemy[target].got_hurt(self.int)
    
  def act(self, my_team, enemy):
    if self.mana < MANA_COST:
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')
    else:
      self.cast(my_team, enemy)


### BERSERKER
class Berserker(Fighter):
  def __init__(self):
    super().__init__()
    self.name = 'Berserker'
    self.cost = 200

  def act(self, my_team, enemy):
    if self.hp <= self.maxhp/2: #take note of hp vs maxhp use hp
      dprint('Berserk mode! Attack double!')
      self.str = 200
      target = rand_alive(enemy)
      dprint(f'Hurt enemy {target} by damage {self.str}.')
      enemy[target].got_hurt(self.str)
      self.str = 100
    else:
      super().act(my_team, enemy) #no need self as its within the char class
      

### ARCHMAGE
class ArchMage(Mage):
  def __init__(self):
    super().__init__() #() empty bracket for super
    self.name='ArchMage'
    self.cost = 600

  def act(self, my_team, enemy):
      if self.mana < MANA_COST:
        self.mana += MANA_RECOVERY
        dprint(f'Mana recover to {self.mana}.')
      else:
        self.cast(my_team, enemy)
        
  def cast(self, my_team, enemy):
    if count_alive(my_team) == 1: 
      self.mana -= MANA_COST
      for i in enemy:
        if i.alive:
          dprint('Cast KABOOM to every enemy!')
          i.got_hurt(self.int*2)
    else:
      super().cast(my_team, enemy)
      
      

### NECROMANCER
class Necromancer(Mage):
  def __init__(self):
    super().__init__()
    self.name = 'Necromancer'
    self.cost = 400

  def act(self, my_team, enemy):
    if self.mana < MANA_COST:
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')
    else:
      self.cast(my_team, enemy)

  def cast(self, my_team, enemy):
    if count_dead(my_team) > 0:
      self.mana -= MANA_COST
      target = rand_death(my_team)
      dprint = (f'Revivng [target] with {my_team[target].maxhp/2} hp')
      my_team[target].alive = True
      my_team[target].hp = my_team[target].maxhp/2
    else:
      super().cast(my_team, enemy)

        
      

















