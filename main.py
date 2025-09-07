import time
userName=""
bag = []
moves = 0
instructions = [
    "get", "grab", "pick", "take", "look", "check", "north", "n", "south", "s",
    "west", "w", "east", "e"
]
lost = False
def livingRoomSpawn():
    key="not got"
    exit = False
    userChoice = ""
    global lost
    global moves
    tableChecked = False
    print("                              N")
    print("                            W + E")
    print("                              S")
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
    print("         |__________________|___|________________|")
    print("                            |   |")
    print("                 fence ->   |   |")
    print("                            |   |")
    print("                 ┌──────────┘   └──────────┐")
    print("                 │                         │")
    print("               shop                  guests' house")
    print("you step into the living room.")
    time.sleep(1)
    print("it looks... beige. this will not do.")
    time.sleep(1)
    print("your friend is coming in a couple hours and you need to gather:\n-friends/guests\n-decorations\n-a cake\n-presents\n-candles")
    print("type north/east/west/south or n/s/e/w to navigate. type 'help' for other instructions")
    while not exit:
        userChoice = str(input("> ")).lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "look" in userChoice and "room" in userChoice:
            print("plain walls, (almost) empty table in the middle. not much to see. (you should probably check out that table)")
            moves+=1
        elif ("look" in userChoice or "check" in userChoice) and "table" in userChoice and not tableChecked:
            print("the house keys lie on the table.")
            tableChecked = True
            moves+=1
        elif ("look" in userChoice or "check" in userChoice) and "table" in userChoice:
            print("?? i already told you? the keys are on the table. just pick them up. smh.")
            moves+=1
        elif "look" in userChoice:
            print("look at what?")
        elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice or "take" in userChoice) and ("key" in userChoice or "it" in userChoice) and key == "not got":        
            print("you take the key. there's a keyring attached, saying LLRL(?). strange.")
            key="got"
            moves+=1
            bag.append("key - says LLRL")
        elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice or "take" in userChoice) and ("key" in userChoice or "it" in userChoice):
            print("you've already got the key")
        elif "e"==userChoice or "east" in userChoice or "s"==userChoice or "south"in userChoice:
            print("you knock yourself out as you walk right into the wall.")
            time.sleep(2)
            print("what was that for? now the party won't be prepared in time")
            exit = True
            gameOver()
        elif "n"==userChoice or "north" in userChoice:
            moves+=1
            print("you move forward in the living room...?")
            time.sleep(1)
            print("that's a bit pointless... remember we've got a time (number of moves) limit!")
        elif "w"==userChoice or "west" in userChoice:
            moves+=1
            exit = True
            hallway()
        else:
            print("idk what you're saying")
def hallway():
    exit = False
    print("you step into the hallway")
    time.sleep(1)
    print("you can go to the:")
    time.sleep(1)
    print("- kitchen")
    time.sleep(1)
    print("- storage room")
    time.sleep(1)
    print("- living room")
    time.sleep(1)
    print("- outside")
    while not exit:
        userChoice = input(str("> ")).lower()
        if "kitchen" in userChoice:
            kitchen()
            exit = True
        elif "storage" in userChoice:
            storage()
            exit = True
        elif "living" in userChoice:
            livingRoom()
            exit = True
        elif "outside" in userChoice and "key - says LLRL" not in bag:
            print("you go outside but you haven't got the keys. you've locked yourself out.")
            time.sleep(2)
            print("yes, it's one of those doors.")
            time.sleep(1)
            print("whoops. ")
            exit = True
            gameOver()
        elif "outside" in userChoice:
            outside()
        else:
            print("pick one out of the list")

def outside():
    print("outside")
def livingRoom():
    print("                              N")
    print("                            W + E")
    print("                              S")
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
    print("         |__________________|___|________________|")
    print("                            |   |")
    print("                 fence ->   |   |")
    print("                            |   |")
    print("                 ┌──────────┘   └──────────┐")
    print("                 │                         │")
    print("               shop                  guests' house")
    print("you step into the living room.")
def kitchen():
    print("                              N")
    print("                            W + E")
    print("                              S")
    print("          _______________________________________")
    print("         |  storage         |   |                |")
    print("         |                                       |")
    print("         |                  |   |                |")
    print("         |_______  _________|   |                |")
    print("         |                  |   |                |")
    print("         |                  │   |   living room  |")
    print("         |     kitchen      |   |                |")
    print("         |      [YOU]                            |")
    print("         |                  │   |                |")
    print("         |__________________|___|________________|")
    print("                            |   |")
    print("                 fence ->   |   |")
    print("                            |   |")
    print("                 ┌──────────┘   └──────────┐")
    print("                 │                         │")
    print("               shop                  guests' house")
def storage():
    print("storage")
def shop():
    print("shop")
def house():
    print('house')

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
    print("you can use 'look' to look at any object or around the room. remember to specify.")
def gameOver():
    time.sleep(3)
    print(" ~~~~~~~~~~~ ")
    print("| GAME OVER |")
    print(" ~~~~~~~~~~~ ")

print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
print(" |         WELCOME :)        |")
print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(2)
print("set up your friend's surprise birthday party before they get here!")
print("type 'help' for instructions")
print("type 'check bag' to look at what's in your bag.")
print("\n")
userName = input(str("enter name: "))
print("have fun, "+userName+"!\n\n")
livingRoomSpawn()