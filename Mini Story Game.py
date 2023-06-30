#This is a text-based mini adventure story game
#Players will have to choose every decision for each step of storyline

def main():
    player =  player_name()
    start_adventure()
    print("\nTHE END\n")
    print("Thanks for playing!")
    
def player_name():
    #Player enters their name
    name = input("What's your name? : ")
    
    #It just for the laughing stock  
    funny_name = "LITTLE PONNY"
    answer = input("Your name is {}, is that correct? [Y/N] : ".format(funny_name.upper()))
    if answer.lower() in ["y","yes"]:
        name = funny_name
        print("Alright. You are fun, {}! lol. Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n","no"]:
        print("Alright picky! {} it is. Let's begin our adventure!".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(funny_name.upper()))
        name = funny_name
 
def start_adventure():
    #Create the dungeon  
    print_dungeon()
    print("You see a red and blue door 👁  👁")
    
    #Gets input from player. Player picks a door 
    pick_door = input("Do u want to pick red or blue door?")
    if pick_door.lower() in ["red","RED", "Red"]:
        facing_fear()
    elif pick_door.lower() in ["blue","BLUE","Blue"]:
        lucky_notlucky()
    else:
        print("Sorry, the answer is either 'Red' or 'Blue'. You are the weakest link! Your adventure ends up here. GOODBYE!")

def facing_fear():
    #Create the monster
    print_monster()
    print("Uh ohh. There you see the EVIL DRAGON.")
    print("It stares at you and you go insane 🤯")
    print("Will you run for your life or eat your head?","[run for my life or eat my head]")
    
    #If player picks Run for my life, they will return to the start of the game, in the room with the red and blue door or die!
    next_thing2do = input("= ")
    if next_thing2do.lower() in ["Run for my life", "run for my life"]:
        start_adventure()
    else:
        you_died("You died. That was tasty!")
    
def you_died(why):
    game_over()
    print("{}. Good job!".format(why))

def lucky_notlucky():
    #Create treasure
    print_treasure() 
    #Stuff in treasure chest
    treasure_chest = ["diamonds", "gold", "silver"]
    print("You notice if there's a room with a chest on the left, and also sleeping guards") 
    print("on the right in front of the door")

    #Asking what the player will do
    print("What will you do? ")
    print("Get to see the treasure? Press '1'")
    print("Leave it? Press '2' ")
    to_do = input("= ")
    print("--------------------------------------------------")
    
    #Making condition about what will happen for each options
    if to_do == "1":
        print("Alright, you are that brave 😱. Let us see what's on the chest....")
        print("The chest opened with a slight squeak while the guard is still sleeping. Such a heavy sleeper")
        print("Woahh, you see the shiney stuff . 。°˙°.。✧₊˚ʚ ᗢ₊˚✧ ﾟ.✧ ")
        
        for treasure in treasure_chest:
            print(treasure)
    
        #There's so much treasures on it. Ask player what to do
        print("What do you wanna do?")
        print("Take all {} treasures, press '1'".format(len(treasure_chest)))
        print("Leave it, press '2'")
        
        choice = input("= ")
        if choice == "1" :
            print("WOHOOO! LOT OF TREASURES! I SHOULD BE A CRAZY RICH AFTER IT 😅.")
            print("OHH, THERE'S ALSO AN EPIC SHINEY SWORD ")
            print("--------------------------------------------------")
        elif choice == "2" :
            print("It should be here still right after I get past these guards (I hope)")
        
        #Take the treasures or Leave it, the player will encounter the guards still
        #calling guard function
        guards()
    
    else:
        print("The guards are more interesting. Let's go that way then")
        guards()

def guards():
    print("The guards are sleeping still while you approach them")
    print("Suddenly you dropped a stuff that you are bring and it makes the guards awake")
    print("GUARDS : HEY! What you are doing here?")
    print_guards()
    
    #Player decides to run or go to the door
    action = input("[run / door] : ").lower()
    if action == "run" :
        print("Guards are faster coming to you and BAM!! Your world goes dark!")
        print("          .-~~-.         ")
        print("         (_~..~_)        ")
        print("           ||||          ")
        print("    __________________   ")
        print(" (____    _||||_    )    ")
        print("   ___)  ( _''_ )  (___  ")
        print("  (_      ~-..-~      _) ")
        print(" ___)                (___ ")
        print("(______  OH NO!! ________) ")
        print("    ___)        (    `      ")
        print("   (_____________)           ")

    elif action == "door" :
        print("You just slipped the door before the guards chase you")
        print("You made it and now you are outside. WAHOO!")
        print("                       _        ")
        print("                     _( }       ")
        print("           -=   _  <<  \     ")
        print("               `.\__/`/\\   ")
        print("         -=      '--'\\  `   ")
        print("              -=     //     ")
        print("                     \)  💨   ")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def print_dungeon():
    #Print dungeon. Inspired by dungeon ASCII design on https://ascii.co.uk/art/dungeon
    print()
    print("     _________________________________________________________   ")  
    print("   /|_-_- _ -_-_-_-_- _ -_-_-_ -_- _ -_-_- _-_-_-_- _ -_-_-_- |\  ")
    print("  / |_-_-                                               -_- _-| \ ")
    print("    |      .-'````````'.        CIP        .-'```````'-.      |")
    print("    |    .`             `.    DUNGEON    .`             `.    |")
    print("    |   /______ red ______\     ツ      /______ blue _____\   |")
    print("    |  |    |              | o   T   o |    |              |  |")
    print("    |  |    |              |  .  |  .  |    |              |  |")
    print("    |  |    |              |   . | .   |    |              |  |")
    print("    |  |    |              |    .|.    |    |              |  |")
    print("    |  |    |______________|     |     |    |___ ;_________|  |  ")
    print("    |  |   /  __ ;   -     |           |   /     `'() _ -  |  |")
    print("    |  |  / __  ()        -|           |  /  __--      -   |  |")
    print("    |  | /        __-- _   |           | /        __--_    |  |")
    print("    |__|/__________________|___________|/__________________|__|")
    print("   /                                             _ -           \ ")
    print("  /   -_- _ -             _- _---                       -_-  -_ \ ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print()

def print_monster():
    #Print monster. Monster ASCII design got inspired by https://oocities.org/spunk1111/haloween.htm)
    print()
    print("\'.                                                           .'/")
    print("   ),\                                                         /,( ")
    print("  /__\'.                                                     .'/__\ ")
    print("    \  `'.'-.__                                           __.-'.'/ ")
    print("   `)   `'-. \                                         / .-'`   (' ")
    print("   /   _.--'\ '.          ,            ,          .' /'--._   \ ")
    print("   |-'`      '. '-.__    / \          / \    __.-' .'      `'-| ")
    print("    \         _.`'-.,_'-.|/\ \    _, / /\|.-'_,.-'`._       /")
    print("`    \    .-'       /'-.|| \ |.-"   "-.| /||.-'\       '-.    /` ")
    print("     )-'`        .'   :||  / -.\\ //.- \ ||:   '.        `'-( ")
    print("    /          .'    / \\_ |  /o`^'o\  | // \    '.          \  ")
    print("     /_.'     .-'  _.-'     \\ \/^\/ //     `-._  '-.     '._\ ' ")
    print("     \     .'`_.--'          \\ 🔻   //          `--._`'.     /  ")
    print("      '-._' /`            _   \\-.-//   _            `\ '_.-'   ")
    print()             
    print("             \  ``--..__   \     `'`     /   __..--``  /_     ")
    print("          /  '-.__     ``'-;    / \    ;-'``     __.-'  \    ")
    print("         |    _   ``''--..  \'-' | '-'/  ..--''``   _    |   ")
    print("         \     '-.       /   |/--|--\|   \       .-'     /   ")
    print("          '-._    '-._  /    |---|---|    \  _.-'    _.-'    ")
    print("             `'-._   '/ / / /---|---\ \ \ \'   _.-'`        ")
    print("                 '-./ / / / \`---`/ \ \ \ \.-'               ")
    print("                       `)` `  /'---'\  ` `(`                  ")
    print("                     /`     |       |     `\            ")
    print("                    /  /  | |       | |  \  \        ")
    print("                .--'  /   | '.     .' |   \  '--.    ")
    print("               /_____/|  / \._\   /_./ \  |\_____\   ")
    print("              (/      (/'     \) (/     `\)      \)    ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def game_over():
    #Game over ASCII text. Generated at http://www.patorjk.com/software/taag/#p=display&f=Small&t=GAME%20OVER 
    print ("   ___   _   __  __ ___    _____   _____ ___  ")
    print("   / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ ")
    print("  | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   / ")
    print("   \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ ")
    print()

def print_treasure():
    #Print treasure chest. Treasure ASCII art design got inspired by https://ascii.co.uk/art/treasure" 
    print()
    print("          ✧₊            _.--. ")
    print("                  _.-'_:-'|| ")
    print("     ✧₊        _.-'_.-::::'||     ✧₊       ")
    print("         _.-:'_.-::::::'  ||     ✧₊    ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("    ✧₊  ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def print_guards():
    #Print guards. Guards ASCII art design inspired by https://ascii.co.uk/art/knights
    print()
    print("            ,;;,.                  ,;'',   ")
    print("             /~\                    /~\    ")
    print("            ([~])                  ([~])  ")
    print("          ,_.~~~.                  .~~~.    ")
    print("        ()--|   ,\                /    ,\    ()   ")
    print("     ,_//   |   |>)              (<|   |\()--'m   ")
    print("  (~'  m''~)(   )/                \(   )   ~~'|   ")
    print("   \(~||~)/ //~\\                  //~\\     ||  ")
    print("      ||   ()   ()      CiP       ()   () /( || )\   ")
    print("      ||   ||   ||       -        ||   ||( '-||-' )  ")
    print("      || ,;.)   (.;,            ,;.)   (.;,(~\/~)/   ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    

if __name__ == "__main__":
    main()
