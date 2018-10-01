###This document is for managing player stats
class Player():
  def __init__(self):

    ###Positional stats and functions
    self.x = 1
    self.y = 2

    ###The players level and XP
    self.xp = 0
    self.level = 1

  #xp algorithm for later:
  """xp_required = 0
     ON LEVEL UP:
     xp_required = xp_required + ( level * 100 )
     xp = 0
     level += 1
     this means that level req will go up by 100 each time"""
    

player = Player()
