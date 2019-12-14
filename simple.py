import random
import time
import sys

def spin():
  animation = "|/-\\"
  for i in range(10):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
  print(" ")
  
class Unit:
  def __init__(self, name, hp, atk):
    self.name = name
    self.hp = hp
    self.atk = atk
    self.alive = True
  def __str__(self):
    return self.name + "(" + str(self.hp) + ")"
  def takeDamage(self, damage):
    self.hp -= damage
    if (self.hp <= 0):
      self.hp = 0
      self.alive = False
  def attack(self, unit):
    unit.takeDamage(self.atk)

class Team:
  def __init__(self, name, units):
    self.name = name
    self.units = units
  def __str__(self):
    rep = "[ "
    for unit in self.units:
      rep += str(unit)
      rep += " "
    rep += "]"
    return rep
  def allDead(self):
    return len(self.units) == 0
  def attack(self, enemies):
    for unit in self.units:
      if enemies.allDead():
        return
      target = enemies.units[random.randrange(0, len(enemies.units), 1)]
      unit.attack(target)
      if not target.alive:
        # print("Unit dead: " + target.name)
        enemies.units.remove(target)

def game():
  our_team = []
  our_team.append(Unit("U_red", 100, 10))
  our_team.append(Unit("U_gre", 90, 12))
  our_team.append(Unit("U_blu", 95, 11))
  our_team.append(Unit("U_yel", 80, 14))

  their_team = []
  their_team.append(Unit("T_red", 100, 10))
  their_team.append(Unit("T_gre", 100, 10))
  their_team.append(Unit("T_blu", 95, 11))
  their_team.append(Unit("T_yel", 90, 14))

  us = Team("us", our_team)
  them = Team("them",their_team)

  while True:
    print("US:   " + str(us))
    print("THEM: " + str(them))
    if us.allDead():
      print("we lost")
      return
    if them.allDead():
      print("we won")
      return
    us.attack(them)
    them.attack(us)
    spin()

game()
