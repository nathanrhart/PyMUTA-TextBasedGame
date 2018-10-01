from commands import *
from fizzler import *
                                                              

print("What would you like to do:")
print("'new' - enter a new game")
print("'load' - load your last saved game")
def startmenu():
  menu_input = input("Option: ")
  if menu_input.lower() in ['new','n']:
    print("Type 'help' to get started")
  elif menu_input.lower() in ['load','l']:
    try:
      print("Trying to load(not really)!")
      print("Loader not built yet, starting a new game!")
      #from save import *
    except:
      print("No save found. Starting a new game!")
      print("Type 'help' to get started")
  else:
    print("Didn't catch that, try again?")
    startmenu()

startmenu()

def play(): #define the main play script
  while True:
    action_input = get_player_command() #get what the player wants to do
    #action_input[0](action_input[1])
      
    #help command: So the user can know whats going on
    if action_input[0] in command_help:
      help(action_input[1]) #if they just typed help on it's own, launch help without args
  
    #go command: So the user can move
    elif action_input[0] in command_go:
      go(action_input[1]) #launch the go command

    #inventory command: To see what he's packin.
    elif action_input[0] in command_inv:
      inv(action_input[1],action_input[2],action_input[3])

    #using the map in the players inventory(if they have one)
    elif action_input[0] in command_map:
      map()

    #used for debugging.. Pay no attention to the man behind the curtain..
    elif action_input[0] in ['debug']:
      debug(action_input[1])

    elif action_input[0] in ['clear']:
      print("\n" * 100)
      
    else: print("Invalid Move! Why not try using help!")

### END OF PLAY FUNCTION ###
if __name__ == '__main__':
  play()
else:
  print("Keep calling me and I'll block your number.")

""" NOTES TO SELF:
########calling inventory by place in list
#print(inventory[1].desc) to print the description of a certain Item
#inventory[1].desc = "NEW DESCRIPTION HERE"

########calling inventory by name
Finding an item
##for i in inventory:
    if i.name == "Item":
      found = 1
      print("Success!")
  if found == 0
    print("Fail!")

Changing an item(lets say the player is dropping one)
##for i in inventory:
    if i.name == "Item" and i.amount > 0:
      found = 1
      i.amount = i.amount - 1
  if found = 0
    print("Fail!")
      
"""
