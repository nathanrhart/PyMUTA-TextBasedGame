"""
########################################
#####    WEAPONS AND ITEMS LIST    #####
########################################

class NAME:
  #self.amount = Amount the player has
  #self.name = String of the item name
  #self.desc = Item description
  #self.damage = Damage the item can do
  #self.accuracy = Chance of item doing damage(THIS IS A PERCENTAGE)
  #self.type = Melee / Ranged etc
"""

#Master List of items:
#Calling everything in the Items db
def inventorylist():
  inventory = []

  #Master list, try to keep alphabetical

  inventory.append(CrustyBread())
  inventory.append(Gold())
  inventory.append(Map())
  inventory.append(Stick())
  inventory.append(Stone())
  inventory.append(StoneAxe())


  #End of master list
  return inventory

######################################

class Item:
  def __str__(self):
    return self.name

######################################

class CrustyBread(Item):
  def __init__(self):
    self.amount = 2
    self.name = "CrustyBread"
    self.desc = "It's not great, might help though"
    self.damage = 1
    self.accuracy = 0.05
    self.type = "Melee"
    
######################################

class Gold(Item):
  def __init__(self):
    self.amount = 5
    self.name = "Gold"
    self.desc = "Currency useful for economy."
    self.damage = 1
    self.accuracy = 0.15
    self.type = "Melee"

####################################

class Map(Item):
  def __init__(self):
    self.amount = 1
    self.name = "Map"
    self.desc = "This will clear things up!"
    self.damage = 1
    self.accuracy = 0.2
    self.type = "Melee"
#####################################
  
class Stick(Item):
  def __init__(self):
    self.amount = 0
    self.name = "Stick"
    self.desc = "A wooden stick, a weapon, a tool, a stick."
    self.damage = 5
    self.accuracy = 0.75
    self.type = "Melee"

#####################################
  
class Stone(Item):
  def __init__(self):
    self.amount = 1
    self.name = "Stone"
    self.desc = "Small fist-sized rock, a bludgeoning weapon or tool."
    self.damage = 5
    self.accuracy = 0.55
    self.type = "Melee"
  
####################################

class StoneAxe(Item):
  def __init__(self):
    self.amount = 0
    self.name = "StoneAxe"
    self.desc = "A bit of a stretch, but it could work."
    self.damage = 10
    self.accuracy = 0.85
    self.type = "Melee"

#####################################
