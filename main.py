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
setUp=False
cakeMoves = 0
cake = "not made"
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
    print("your friend is coming in 4 hours and you need to gather:\n-friends/guests\n-decorations\n-a cake\n-presents\n-candles")
    print("type north/east/west/south or n/s/e/w to navigate. type 'help' for other instructions")
    while not exit:
        userChoice = input(f"(hours gone by: {moves}) > ").lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "look" in userChoice and ("room" in userChoice or "around" in userChoice):
            print("plain walls, (almost) empty table in the middle. not much to see. (you should probably check out that table)")
            moves+=0.25
        elif ("look" in userChoice or "check" in userChoice) and "table" in userChoice and not tableChecked:
            print("the house keys lie on the table.")
            tableChecked = True
            moves+=0.25
        elif ("look" in userChoice or "check" in userChoice) and "table" in userChoice:
            print("?? i already told you? the keys are on the table. just pick them up. smh.")
            moves+=0.25
        elif "look" in userChoice:
            print("look at what?")
        elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice or "take" in userChoice) and ("key" in userChoice or "it" in userChoice) and key == "not got":        
            print("you take the key. there's a keyring attached, saying LLRL(?). strange.")
            key="got"
            moves+=0.25
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
            moves+=0.25
            print("you move forward in the living room...?")
            time.sleep(1)
            print("that's a bit pointless... remember we've got a time (number of moves) limit!")
        elif "w"==userChoice or "west" in userChoice:
            moves+=0.25
            exit = True
            hallway()
        else:
            print("i don't know what you're saying. try something else?")
def hallway():
    exit = False
    global moves
    print("you step into the hallway")
    time.sleep(1)
    print("you can go to the:")
    time.sleep(1)
    print("- kitchen")
    time.sleep(1)
    if "candles" not in bag:
        print("- storage room")
        time.sleep(1)
    print("- living room")
    time.sleep(1)
    print("- outside")
    while not exit:
        userChoice = input(f"(hours gone by: {moves}) > ").lower()
        if "kitchen" in userChoice:
            moves+=0.25
            exit = True
            kitchen()
        elif "storage" in userChoice:
            if "candles" not in bag:
                moves+=0.25
                exit = True
                cat()
            else:
                print("you can't go there anymore.")
        elif "living" in userChoice:
            moves+=0.25
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
            moves+=0.25
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
    global moves
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
        userChoice = input(f"(hours gone by: {moves}) > ").lower()
        if "shop" in userChoice:
            moves+=0.25
            exit = True
            shop()
        elif "house" in userChoice:
            moves+=0.5
            exit = True
            house()
        elif "hall" in userChoice:
            moves+=0.25
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
    global setUp
    global moves
    win=False
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
    if ("cake (yum!)" not in bag or "deco" not in bag or "candles" not in bag or "present" not in bag) and friends=="not got":
            print("you haven't got all of the stuff! come back when you get cake, deco, candles, and presents. (and preferably friends)")
            exit=True
            hallway()
    elif ("cake (yum!)" not in bag or "deco" not in bag or "candles" not in bag or "present" not in bag):
            print("you haven't got all of the stuff! come back when you get cake, deco, candles, and presents.")
            exit=True
            hallway()
    elif friends == "not got":
        print("you can set this up all by yourself rn (and then go invite friends) or go and get your friends right now to help.")
    while not exit and moves<8 and not win:
        userChoice=input(f"(hours gone by: {moves}) > ").lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "hallway" in userChoice or "west" in userChoice or "w"==userChoice:
            exit=True
            moves+=0.25
            hallway()
        elif "set" in userChoice and setUp:
            print("you've already set up! go and invite friends")
        elif "set" in userChoice and friends=="not got":
            print("it takes you a long time to get the stuff set up... (let's hope you didn't spend too much time on other stuff)")
            moves+=4
            setUp=True
        elif "set" in userChoice and friends == "got":
            print("you set up everything quickly with your friends!")
            time.sleep(2)
            print("the living room is ready. the cake is on table (with candles!), the decorations are hung up, the presents are left by the door.")
            time.sleep(2)
            print("you and your friends are giggling behind a sofa when you hear footsteps.")
            time.sleep(2)
            print("the sound of the key turning silences everyone...")
            time.sleep(2)
            print("   ~~~~~~~~~~~~~~~~~~~")
            print("  |     SURPRISE!!    |")
            print("   ~~~~~~~~~~~~~~~~~~~")
            print("your friend's face lights up. 'wow,",userName+"! thank you so much :) this is the best surprise i could have asked for!'")
            time.sleep(2)
            if cake=="taken":
                print("they spot the cake, saying, 'oh and you even home-baked a cake for me!'")
            win=True
        else:
            print("sorry! i don't  know what you're saying, try something else?")
    if not exit:
        if moves<=8 and win:
            time.sleep(2)
            endWin()
        if moves>8 and friends=="not got":
            print("you hear a key turn in the door.")
            time.sleep(2)
            print("oh no nono!!!")
            time.sleep(1)
            print("the decoration is still in its packet, the candles aren't on the cake yet, and your friends aren't even here!")
            time.sleep(3)
            print("your birthday friend walks in, sees the mess that you've made, and freezes.")
            time.sleep(2)
            print("before you can say anything, you're pulled into a hug.")
            time.sleep(1)
            print("they laugh, 'you tried surprising me, didn't you? this is the best surprise i could have asked for.'")
            if cake=="taken":
                print("they spot the cake, saying, 'oh and you even home-baked a cake for me!'")
            time.sleep(2)
            print("you both go to your friends' house to invite them over, and everyone spends the day talking and eating cake.")
            time.sleep(2)
            print("it wasn't perfect, but that doesn't matter when your friends are with you :)")
            endWin()
        elif moves>4:
            print("you hear a key turn in the door.")
            time.sleep(2)
            print("oh no nono!!!")
            time.sleep(1)
            print("the decoration are still being put up, the candles aren't on the cake yet, and the presents aren't wrapped!")
            time.sleep(3)
            print("your birthday friend walks in, sees the mess that you've made, and freezes.")
            time.sleep(2)
            print("before you can say anything, you're pulled into a hug.")
            time.sleep(1)
            print("they laugh, 'you all tried surprising me, didn't you? this is the best surprise i could have asked for.'")
            time.sleep(1)
            if cake=="taken":
                print("they spot the cake, saying, 'oh and you even home-baked a cake for me!'")
            endWin()

def kitchen():
    global moves
    exit = False
    global cake
    global cakeMoves
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
    if "cake (yum!)" not in bag:
        print("you can try baking your own cake here! just remember it'll take time.")
        time.sleep(2)
        print("OR you can make the batter (still takes time) and put it in the oven while you go do other stuff. remember to take the cake out the oven if you do that!")
    else:
        print("this *would* be where you could bake a cake but you've already got a cake so you don't really need to be here")
        exit=True
        hallway()
    if cake=="in oven" and moves-cakeMoves>2:
            cake=="burnt"
            print("your cake burnt. :(")
            bag.add("cake (burnt...)")
    while not exit:
        userChoice = input(f"(hours gone by: {moves}) > ").lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
                bagCheck()
        elif "bag" in userChoice:
                print('do what with the bag?')
        elif "help" in userChoice:
                help()
        elif "bake" in userChoice and cake=="not made":
            cake="made"
            print("you make the batter and put it in the oven. do you want to wait here until it's done or leave?")
            moves+=1
        elif "bake" in userChoice and cake=="made":
            print("you've already baked it! it's in the oven")
        elif "wait" in userChoice and cake=="made":
            print("an hour passes.")
            time.sleep(2)
            print("you take out the cake")
            moves+=1
            cake="taken"
            bag.append("cake (yum!)")
            time.sleep(1)
            print("cake acquired, you walk back into the hallway.")
            time.sleep(1)
            exit=True
            hallway()
        elif "wait" in userChoice and cake=="not made":
            print("wait for what?")
            move+=0.5
        elif ("leave" in userChoice or "east" in userChoice) and cake=="made":
            print("ok, make sure to come back in an hour or two. do NOT burn the cake.")
            cakeMoves= moves
            exit=True
            cake="in oven"
            hallway()
        elif cake=="in oven" and moves-cakeMoves >0.5 and moves-cakeMoves<=2:
            print("you take out the cake from the oven.")
            time.sleep(1)
            print("perfect. you ice it, and carefully place it in your bag (let's pretend this is possible to do without it getting squished)")
            cake="taken"
            bag.append("cake (yum!)")
            time.sleep(2)
            print("cake acquired, you walk back into the hallway")
            time.sleep(1)
            exit=True
            hallway()
        elif "east" in userChoice:
            print("going without making a cake? ok! make sure to get some from the shops then.")
            exit=True
            hallway()
        else:
            print("not sure what you mean... try something else.")
def cat():
    global moves
    exit=False
    path=""
    pathValid=False
    catHiss = 0
    print("    |\      _,,,---,,_")
    print("    /,`.-'`'    -.  ;-;;,_")
    print("   |,4-  ) )-,_. ,\ (  `'-'     ")    
    print("  '---''(_/--'  `-'\_)  (ART BY FELIX LEE!!)")
    print("\na cat is sprawled in front of the door of the storage room.")
    time.sleep(2)
    print("the only way to get in is to pet her in the right pattern. every wrong move adds 0.25 to the time taken")
    for loopCount in range(1,5):
        if loopCount==3:
            correctAns="right"
            correctLetter="r"
            wrongAns="left"
            wrongLetter="l"
        else:
            correctAns="left"
            correctLetter="l"
            wrongAns="right"
            wrongLetter="r"
        pathValid=False
        while not pathValid:
            path = input(f"(hours:{moves}) do you pet behind her left ear or right? ").lower()
            if wrongAns in path or wrongLetter==path:
                print("you pet her wrong ear and the cat hisses at you.")
                time.sleep(1)
                moves+=0.25
                catHiss+=1
                pathValid=True
            elif ("check" in path or "look" in path) and "bag" in path:
                bagCheck()
            elif "help" in path:
                print("type left/l or right/r")
            elif correctAns in path or correctLetter==path:
                print("you pet behind the",correctAns,"ear and the cat purrs contentedly")
                pathValid=True
            else:
                print("i don't understand. sorry.")
        if catHiss>=2:
            print("the cat hissed at you TWICE")
            time.sleep(1)
            print("i can't believe you'd bother the poor cat like that.")
            time.sleep(1)
            print("you lose for doing that.")
            gameOver()
    storage()
def storage():
    global moves
    looked=False
    print("                              N")
    print("                            W + E")
    print("                              S")
    print("          _______________________________________")
    print("         |     storage      |   |                |")
    print("         |      [YOU]                            |")
    print("         |                  |   |                |")
    print("         |__________________|   |                |")
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
    while "candles" not in bag:
        userChoice=input(f"(hours gone by: {moves}) > ").lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
            print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "look" in userChoice and "harder" in userChoice:
            print("oh! you found some candles!")
            moves+=0.5
            looked=True
        elif "look" in userChoice:
            print("hmmm... bags, old newspapers, duct tape.... (look harder?)")
        elif "candle" in userChoice and not looked:
            print("? what candles? you haven't even found them...")
        elif "candle" in userChoice and looked:
            print("you get the candles and put them in your bag")
            bag.append("candles")
            moves+=0.25
        elif ("east" in userChoice or "leave" in userChoice or "e"== userChoice) and "candles" not in bag and warning==0:
            print("don't leave... it's important to pick something up from here before you go...")
            warning+=1
        elif ("east" in userChoice or "leave" in userChoice or "e"== userChoice) and "candles" not in bag:
            print("nope. you can't leave. try looking around.")
            warning+=1
        else:
            print("i don't know what you said. try again :(")
    hallway()
def shop():
    global moves
    exit = False
    candleCheck = 0
    global cake
    print("you enter the corner shop")
    time.sleep(1)
    print("there's cake and decoration and wonderful presents!") 
    time.sleep(2)
    print("but... no candles...?")
    time.sleep(1)
    print("you could look for them if you *need* to.")
    while not exit:
        userChoice=input(f"(hours gone by: {moves}) > ").lower()
        if ("check" in userChoice or "look" in userChoice) and "bag" in userChoice:
            bagCheck()
        elif "bag" in userChoice:
                print('do what with the bag??')
        elif "help" in userChoice:
            help()
        elif "look" in userChoice and "candle" in userChoice and candleCheck==0:
            moves+=0.25
            if "candles" not in bag:
                print("hmm... none over here. you could try again?")
                candleCheck+=1
            else:
                print("you already have candles! stop looking for them, you'll waste time.")
        elif "look" in userChoice and "candle" in userChoice and candleCheck==1:
            moves+=1
            print("none in the other aisle either.")
            print("maybe ask the shopkeeper (or keep trying)")
            candleCheck+=0.25
        elif "look" in userChoice and "candle" in userChoice and candleCheck>1:
            moves+=0.25
            print("ok, you're wasting time now. either ask the shopkeeper or give up trying to find candles.")
        elif "ask" in userChoice:
            moves+=0.25
            print("the shopkeeper shrugs. 'candles are out of stock.'")
        elif "buy" in userChoice and "present" in userChoice and "present" not in bag:
            moves+=0.25
            print("you buy a present. you put it in your bag")
            bag.append("present")
        elif "buy" in userChoice and "present" in userChoice:
            print("you already have a present!")
        elif "buy" in userChoice and "deco" in userChoice and "deco" not in bag:
            moves+=0.25
            print("you buy decoration. you put it in your bag")
            bag.append("deco")
        elif "buy" in userChoice and "deco" in userChoice:
            print("you already have deco!")
        elif "cake" in userChoice and "buy" in userChoice and "cake (yum!)" not in bag and cake!="in oven":
            moves+=0.25
            print("you buy a cake. you (carefully) put it into your bag")
            bag.append("cake (yum!)")
        elif "cake" in userChoice and "buy" in userChoice and "cake (yum!)" in bag:
            print("you already have cake")
        elif "cake" in userChoice and "buy" in userChoice and cake=="in oven":
            print("you have a cake in the oven.")
        elif "buy" in userChoice:
            print("buy what?")
        elif "leave" in userChoice or "north" in userChoice or "n"== userChoice:
            exit = True
            moves+=0.5
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
    quit()
def endWin():
    print(" ~~~~~~~~~~ ")
    print("| YOU WIN! |")
    print(" ~~~~~~~~~~ ")

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