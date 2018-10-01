#Get the players input on what to do
from items import * #import all the things from all the items
from mapmanager import *
from playermanager import *
inventory = inventorylist()#inventorylist shouldn't be called again.
helpscript = ("Invalid command, type 'help' for a hand!")

def get_player_command():#when the game wants to see what the players gon' do.
  playercommand = (input("Action: ")).lower().split(" ")
  while len(playercommand) < 4:#this makes sure the user always sends 4 arguments
    playercommand.append("")#add the blank arguments
  while len(playercommand) > 4:#if the user inputted more than 4 'args'
    playercommand.pop()#removing any extras they may put
  return playercommand
  #then lower cases the input, and splits it to take multiple arguments

#ARGUMENTS FOR DIFFERENT COMMANDS:
###HELP ARGS
command_help = ['help','h','?']

###GO ARGS
command_go = ['go','g','move','m']
command_go_north = ['north','n','up','u']
command_go_east = ['east','e','right','r']
command_go_south = ['south','s','down','d']
command_go_west = ['west','w','left','l']

###INV ARGS
command_inv = ['inv','i','inventory']
command_inv_inspect = ['inspect','i','in','ins','insp','desc']

###MAP ARGS
command_map = ['map','m']

"""IT'S IMPORTANT THE ARGUMENTS TO LAUNCH THE COMMANDS GO ABOVE"""

### help command
def help(arg0):
  if arg0 == "":#if there is no argument(they just typed help on it's own)
    print("These are the available commands: ")
    print("go")
    print("help")
    print("inv")
    print("You can type help 'command' for more information")
    
  elif arg0 in command_go:#if they type 'help go'
    print("go, g, or move command:")
    print("Use this command to move your player, arguements:")
    print("n, north, or up")
    print("e, east, or right")
    print("s, south, or down")
    print("w, west, or left")
    
  elif arg0 in command_help: #if they  type 'help help'
    print("help, h, or ? command")
    print("You just help help'd..")
    print("I.. I... Nevermind.")

  elif arg0 in command_inv:
    print("inv, i, or inventory")
    print("here you can manage what you're carrying:")
    print("inv inspect [ITEM] - gives you a detailed look of an item")
    
  else: print(helpscript)


### go command
def go(arg0):
      if arg0 in command_go_north:#if the player uses go north
        if checkmap(player.x, player.y-1) == True:#and the space above the player is free
          player.y -=1 #set the players position up one
      elif arg0 in command_go_east:
        if checkmap(player.x+1, player.y) == True:
          player.x += 1
      elif arg0 in command_go_south:
        if checkmap(player.x, player.y+1) == True:
          player.y += 1
      elif arg0 in command_go_west:
        if checkmap(player.x-1, player.y) == True:
          player.x -= 1
            
      else: print("Pick a direction, such as north, east, south or west!")


### inv command
def inv(arg0,arg1,arg2):
  if arg0 == "": #if they user types 'inv'
  #printing the list of items the character has
    #print(inventory[1].name)
    inventoryoutput = []
    for i in inventory: #for each item in inventory
      if i.amount > 0: #and the character actually has one of these
        inventoryoutput.append(str(i) +"("+ str(i.amount) +")" )#find name and amount
    print("Inventory: ")
    for i in inventoryoutput: #this prints the list in a pretty way
      print("~ " + str(i)) #in a Item(#)\n format

  elif arg0 in command_inv_inspect:
    found = 0
  #printing the description for the item the user types
    for i in range(0,len(inventory)): #for each item in inventory
      if inventory[i].name.lower() == arg1:#if the name(lowercase) is the argument
        if inventory[i].amount > 0:#and this argument is in the player inv
          print(inventory[i].desc)#print it's description
          found = 1#tell the system it's found it
    if found == 0:#if it can't find it
      print("I can't find that I'm afraid!")
    if arg2 != "":#if the user accidentally inputted 2 arguments after command
      print("Did you accidentally put a space in the item name?")

  else: print(helpscript)#if all else, blanket statement

### map command
#MAP PRINTER
def map():
  foundmap = 0#start off with saying we haven't got a map
  mapprint = ""#printing nothing
  for i in inventory:#for everyitem in the inventory
    if i.name == "Map" and i.amount > 0:#if one of them is a map
      count = 0 #set the count to zero
      foundmap = 1 #whoop the player has a map
      columns = map_square_size #number to divide and count by, from map size
      for i in range( 0, int(len(mapdata)/columns)):#for everything starting at 0, to the map max x axis
        count = 1 #start with the first row
        #so this is a bit annoyingly complicated, but basically:
        """TAKE THE CURRENT MAP PRINT: ADD x=0y=0, then x=1y=0 etc until end of row, THEN add a new line
            at the end of the row, add one to the count to start x=0y=1, etc. etc."""
        mapprint = mapprint + ( str(mapdata [ (i*count*columns) : (i*count*columns)+columns ] ) + "\n")
        count += 1
#fun characters: █
  mapprint = mapprint.replace(" ","")#parsing the list to make it pretty
  mapprint = mapprint.replace("W"," ")
  mapprint = mapprint.replace("'","")#replacing the list syntaxes with nothing
  mapprint = mapprint.replace(",","")#debug map will show you why these need removing
  mapprint = mapprint.replace("[","")
  mapprint = mapprint.replace("]","")
  if foundmap == 1:#woohoo we found a map
    print(mapprint)#go ahead and print our new pretty map
  else:
    print("You don't have a map!")#oh no, you don't gots a map.

### debug command
def debug(arg0):
  print("nosey cunt aren't you.")
  if arg0 in command_inv:
    sortedinvlist = []
    counter = 0
    for i in inventory:
      print(str(counter) + ". " + str(i))
      counter += 1
  if arg0 == "map":
    print(mapdata)
  if arg0 == "pos":
    print(str(player.x) + ", " + str(player.y))

#for i in range(0,len(mapdata)):
#  print(mapdata[i].name)
