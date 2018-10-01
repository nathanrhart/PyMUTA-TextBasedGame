#MAP GENERATOR####
map_square_size = 16
"""

mapdata = []
for i in range(0,map_square_size^2):#make a 16x16 map (256 tiles)
  mapdata.append("#")
print(mapdata)
"""


#MAP Classes####
class MapTile:
  def __str__(self):
    return self.name

class SpawnTile(MapTile):
  def __init__(self):
    self.name = "0"
    self.discovered = 0
  def walkon(self):
    if self.discovered==0:
      return """
      Welcome to PyMuta!
      """
      self.discovered = 1

  def lookat(self):
    return("This looks like where you started!")

class StandardTile(MapTile):
  def __init__(self):
    self.name = "1"
    self.discovered = 0
  def walkon(self):
    if self.discovered == 0:
      print("I haven't been scripted yet!")
      self.discovered = 1

class ShopTile(MapTile):
  def __init__(self):
    self.name = "S"
    self.discovered = 0
  def walkon(self):
    if self.discovered == 0:
      print("I haven't been scripted yet!")
      self.discovered = 1

class CraftTile(MapTile):
  def __init__(self):
    self.name = "C"
    self.discovered = 0
  def walkon(self):
    if self.discovered == 0:
      print("I haven't been scripted yet!")
      self.discovered = 1

class FurnaceTile(MapTile):
  def __init__(self):
    self.name = "F"
    self.discovered = 0
  def walkon(self):
    if self.discovered == 0:
      print("I haven't been scripted yet!")
      self.discovered = 1

class BossTile(MapTile):
  def __init__(self):
    self.name = "B"
    self.discovered = 0
  def walkon(self):
    if self.discovered == 0:
      print("I haven't been scripted yet!")
      self.discovered = 1

class DeadTile(MapTile):
  def __init__(self):
    self.name = "#"
    self.discovered = 0
  def walkon(self):
    print("How did you get here?")

Z = SpawnTile()
X = StandardTile()
S = ShopTile()
C = CraftTile()
F = FurnaceTile()
B = BossTile()
W = DeadTile()

#MAP DATA
mapdata = [
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','$','W','1','W','W','W','W','W','1','W','W','W','W','W',
'W','0','1','1','1','1','1','1','1','1','1','B','W','W','W','W',
'W','W','C','W','F','W','W','W','W','W','1','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W',
'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W']


###MAP CODES:
"""
This is the space in code for checking the map for events
W = Deadzone
0 = Spawn
1 = Unfound
2 = Found Item
3 = Found enemy

###Special Events
S = Merchant / Shopkeeper
C = Crafting spot
F = Furnace Spot
B = Bossfight
"""
blockedtiles = [W] #tiles the player can't walk on (yet?)

#This is a function to check if the player can move in the first place!
def checkmap(x,y):
  mappos = (x)+(map_square_size*y)
  if mapdata[mappos] in blockedtiles:
    print("You can't find a way through")
    return(False)
  else: return True
