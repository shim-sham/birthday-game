import time
userName=""
bag = []
moves = 0
instructions = [
    "get", "grab", "pick", "take", "look", "check", "north", "n", "south", "s",
    "west", "w", "east", "e"
]
lost = False
friends="not got"
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
            print("i don't know what you're saying. try something else?")
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
            moves+=1
            exit = True
            kitchen()
        elif "storage" in userChoice:
            moves+=1
            exit = True
            storage()
        elif "living" in userChoice:
            moves+=1
            exit = True
            livingRoom()
        elif "outside" in userChoice and "key - says LLRL" not in bag:
            print("you go outside but you haven't got the keys. you've locked yourself out.")
            time.sleep(2)
            print("yes, it's one of those doors.")
            time.sleep(1)
            print("whoops. ")
            exit = True
            gameOver()
        elif "outside" in userChoice:
            exit = True
            moves+=1
            outside()
        elif ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        else:
            print("pick one out of the list")

def outside():
    exit = False
    print("you're outside!")
    print("you can go to the:")
    time.sleep(1)
    print("- shop")
    time.sleep(1)
    print("- guests' house")
    time.sleep(1)
    print("- hallway")
    while not exit:
        userChoice = input(str("> ")).lower()
        if "shop" in userChoice:
            moves+=1
            exit = True
            shop()
        elif "house" in userChoice:
            moves+=1
            exit = True
            house()
        elif "hall" in userChoice:
            moves+=1
            exit = True
            hallway()
        elif ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        else:
            print("pick one out of the list")

def livingRoom():
    exit = False
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
    if "cake (yum!)" not in bag or "deco" not in bag or "candles" not in bag or "present" not in bag:
            print("you haven't got all of the stuff! come back when you get cake, deco, candles, presents")
            exit=True
            hallway()
    elif friends == "not got":
        print("you can set this up all by yourself rn (and then go invite friends) or go and get your friends right now to help.")
    while not exit:
        userChoice=input(str("> ")).lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "set" in userChoice and friends=="not got":
            print("it takes you a long time to get the stuff set up... (let's hope you didn't spend too much time on other stuff)")
            moves+=4
        elif "set" in userChoice and friends == "got":
            print("you set up everything quickly with your friends!")
        else:
            print("sorry! i don't  know what you're saying, try something else?")
def kitchen():
    global moves
    exit = False
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
    global moves
    exit = False
    print("                              N")
    print("                            W + E")
    print("                              S")
    print("          _______________________________________")
    print("         |     storage      |   |                |")
    print("         |      [YOU]                            |")
    print("         |                  |   |                |")
    print("         |_______  _________|   |                |")
    print("         |                  |   |                |")
    print("         |                  │   |   living room  |")
    print("         |     kitchen      |   |                |")
    print("         |                                       |")
    print("         |                  │   |                |")
    print("         |__________________|___|________________|")
    print("                            |   |")
    print("                 fence ->   |   |")
    print("                            |   |")
    print("                 ┌──────────┘   └──────────┐")
    print("                 │                         │")
    print("               shop                  guests' house")
    print("you enter the storage room.")
    while not exit:
        userChoice=input(str("> ")).lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
                bagCheck()
        elif "bag" in userChoice:
                print('do what with the bag??')
        elif "help" in userChoice:
                help()
def shop():
    global moves
    exit = False
    candleCheck = 0
    print("you enter the corner shop")
    time.sleep(1)
    print("there's cake and decoration and wonderful presents!") 
    time.sleep(2)
    print("but... no candles...?")
    time.sleep(1)
    print("you could look for them if you need to.")
    while not exit:
        userChoice=input(str("> ")).lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
                print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "look" in userChoice and "candle" in userChoice and candleCheck==0:
            moves+=1
            if "candles" not in bag:
                print("hmm... none over here. you could try again?")
                candleCheck+=1
            else:
                print("you already have candles! stop looking for them, you'll waste time.")
        elif "look" in userChoice and "candle" in userChoice and candleCheck==1:
            moves+=1
            print("none in the other aisle either.")
            print("maybe ask the shopkeeper (or keep trying)")
            candleCheck+=1
        elif "look" in userChoice and "candle" in userChoice and candleCheck>1:
            moves+=1
            print("ok, you're wasting time now. either ask the shopkeeper or give up trying to find candles.")
        elif "ask" in userChoice:
            moves+=1
            print("the shopkeeper shrugs. 'candles are out of stock.'")
        elif "buy" in userChoice and "present" in userChoice and "present" not in bag:
            moves+=1
            print("you buy a present. you put it in your bag")
            bag.append("present")
        elif "buy" in userChoice and "present" in userChoice:
            moves+=1
            print("you already have a present!")
        elif "buy" in userChoice and "deco" in userChoice and "deco" not in bag:
            moves+=1
            print("you buy decoration. you put it in your bag")
            bag.append("deco")
        elif "buy" in userChoice and "deco" in userChoice:
            moves+=1
            print("you already have deco!")
        elif "cake" in userChoice and "buy" in userChoice and "cake (yum!)" not in bag:
            moves+=1
            print("you buy a cake. you (carefully) put it into your bag")
            bag.append("cake (yum!)")
        elif "cake" in userChoice and "buy" in userChoice:
            moves+=1
            print("you already have cake")
        elif "buy" in userChoice:
            print("buy what?")
        elif "leave" in userChoice or "north" in userChoice or "n"== userChoice:
            exit = True
            outside()
        else:
            print("i don't know what you're saying. try something else?")
def house():
    global moves
    exit = False
    print('house')

def bagCheck():
    bagCount=1
    global moves
    moves+=1
    for item in bag:
        print(bagCount,item)
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
time.sleep(1)
print("set up your friend's surprise birthday party before they get here!")
print("type 'help' for instructions")
print("type 'check bag' to look at what's in your bag.")
print("\n")
userName = input(str("enter name: "))
print("have fun, "+userName+"!\n\n")
livingRoomSpawn()