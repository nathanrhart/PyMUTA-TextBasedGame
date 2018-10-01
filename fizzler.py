from random import *

pymuta = ("\
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n\
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n\
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  \n\
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  \n\
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗\n\
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\n\
                                                              \n\
                      ████████╗ ██████╗                       \n\
                      ╚══██╔══╝██╔═══██╗                      \n\
                         ██║   ██║   ██║                      \n\
                         ██║   ██║   ██║                      \n\
                         ██║   ╚██████╔╝                      \n\
                         ╚═╝    ╚═════╝                       \n\
                                                              \n\
   ██████╗ ██╗   ██╗███╗   ███╗██╗   ██╗████████╗ █████╗      \n\
   ██╔══██╗╚██╗ ██╔╝████╗ ████║██║   ██║╚══██╔══╝██╔══██╗     \n\
   ██████╔╝ ╚████╔╝ ██╔████╔██║██║   ██║   ██║   ███████║     \n\
   ██╔═══╝   ╚██╔╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══██║     \n\
   ██║        ██║   ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║     \n\
   ╚═╝        ╚═╝   ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝     \n")

refreshrate = 4000

def find_highest():#use this to find the highest unicode value
  highest = 0
  for i in pymuta:
    if ord(i) > highest:
      highest = ord(i)
  return(highest)
find_highest()
print("Highest unicode Number form: " + str(find_highest()))
print("Highest unicode String form: " + chr(find_highest()))
#find_highest()
def find_lowest():
  lowest = find_highest()
  for i in pymuta:
    if ord(i) not in [10,32,34]:
      if ord(i) < lowest:
        lowest = ord(i)
  return(lowest)
print("Lowest unicode Number form: " + str(find_lowest()))
print("Lowest unicode String form: " + chr(find_lowest()))

def scrambler(input):
  highest = find_highest()
  lowest = find_lowest()
  scrambled = []
  for i in range(len(input)):
    scrambled.append(" ")
  out = scrambled
  output = out
  printcounter = 0
  
  finished = False
  while output != list(input):
    for i in range(0,len(input)):
      if input[i] in [chr(10),chr(32),chr(34)]:
        output[i] = input[i]
      if output[i] != input[i]:
        madeupnum = randint(lowest,highest)
        madeupchr = chr(madeupnum)
        scrambled[i] = madeupchr
      elif scrambled[i] == input[i]:
        output[i] = input[i]
      printcounter += 1
      if printcounter == refreshrate:
        print("\n" * 20)
        print("".join(output))
        printcounter = 0
  print("\n" * 20)
  print("".join(output))

    
scrambler(pymuta)
    
  
