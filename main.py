import time
userName=""
bag = []
moves = 0
instructions = [
    "get", "grab", "pick", "take", "look", "check", "north", "n", "south", "s",
    "west", "w", "east", "e"
]
def livingRoomSpawn():
    print("          _______________________________________")
    print("         |  storage         |   |                |")
    print("         |                                       |")
    print("         |                  |   |                |")
    print("         |_______  _________|   |                |")
    print("         |                  |   |                |")
    print("         |                  │   |   living room  |")
    print("         |     kitchen      |   |                |")
    print("         |                             [YOU]     |")
    print("         |                  │   |                |")
    print("         |______________________|________________|")
    print("                            |   |")
    print("                 fence ->   |   |")
    print("                            |   |")
    print("                 ┌──────────┘   └──────────┐")
    print("                 │                         │")
    print("               shop                  guests' house")
    print("you look around the empty living room. ")
    time.sleep(1)
    print("you really need to decorate this place.")
    time.sleep(1)
    print("your friend is coming in 4 hours and you need to gather:\n-friends/guests\n-decorations\n-a cake\n-presents\n-candles")
    print("type north/east/west/south or n/s/e/w to navigate.")


def bagCheck():
    bagCount=1
    global moves
    moves+=1
    for item in bag:
        print(bagCount,"-",item)
        bagCount+=1
    if len(bag)==0:
        print("you haven't got anything in your bag!")
def help():
    global instructions
    print("the instructions i know are:")
    for instruction in instructions:
        print("-",instruction)
print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
print(" |         WELCOME :)        |")
print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("set up your friend's surprise bday party before they get here!")
print("type 'help' for instructions")
print("type 'check bag' to look at what's in your bag.")
print("\n")
userName = input(str("enter name: "))
print("have fun, "+userName+"!\n\n")
livingRoomSpawn()