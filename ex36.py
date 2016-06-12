from sys import exit

def start():
    print "\nWelcome to Winterfell! You are Jon Snow,"
    print "illegitimate son of Eddard \"Ned\" Stark,"
    print "Warden of the North and Lord of Winterfell.\n"
    first_move()

def first_move():
    print "Now that your father is heading to King\'s Landing, do you:"
    print "- HEAD NORTH to Castle Black to join the Night's Watch"
    print "- HEAD SOUTH to King\'s Landing to follow your father"
    print "- STAY PUT in Winterfell and sentry the castle.\n"

    print "Type in your choice option using the text in ALL CAPS."

    choice = raw_input("> ")
    choice.lower()

    if choice == "head north":
        castle_black_arrival()
    elif choice == "head south":
        kings_landing()
    elif choice == "stay put":
        winterfell()
    else:
        print "\nSorry, I do not understand. Try again!\n"
        first_move()

def castle_black_arrival():
    print "\nArya (your half-sister): \"Don't leave, Jon! I'll miss you!\""
    print "Cat (your stepmother): \"Begone with ye, spawn of a whore.\""
    print "You ride off to Castle Black in search of glory.\n"

    print "Once you arrive, you feel a sudden sense of dread"
    print "as you meet three people: SAM, a morbidly obese new recruit,"
    print "THORNE, a angry-looking senior ranger of the Night\'s Watch,"
    print "and BENJEN, your uncle and First Ranger of the Night's Watch.\n"
    castle_black_start()

def castle_black_start():
    print "To whom do you speak with: SAM, THORNE, or BENJEN?"

    choice = raw_input("> ")
    choice.lower()

    if choice == "sam":
        samwell_tarly()
    elif choice == "thorne":
        print "\nThorne: \"I ain't got time to talk to new recruits, least of all bastards. \nGo on, find someone else to bother, \'Lord Snow\'...\"\n"
        castle_black_start()
    elif choice == "benjen":
        print "\nBenjen: \"Welcome, nephew. Unfortunately I ride at first light, \nso I am unable to talk at the moment. Go meet the other new recruits.\"\n"
        castle_black_start()
    else:
        print "\nSorry, I do not understand. Try again!\n"
        castle_black_start()

def samwell_tarly():
    print "\nSam: \"It's a p-p-pleasure to meet you.\"\n"
    print "Sam trembles as he extends his hand to you, which you politely shake."
    print "Out of the corner of your eye, you see three others approaching."
    print "The largest one, RAST, looks particularly menacing.\n"

    print "Rast: \"Why, look at that! Our little black piggie has made a friend! \nCome on, then. If you like \'em big, you're going to love me!\"\n"
    rast_attack()

def rast_attack():

    print "What do you want to do to Rast: TALK BACK, PUNCH, or STARE DOWN?"

    choice = raw_input("> ")
    choice.lower()

    if choice == "talk back":
        print "\nYou: \"Why don\'t you leave us alone and play with your buddies?\""
        print "Rast: \"Oh, we're about to do just that. \nA little game we call 'Get The Bastard'!\"\n"
        dead("Rast and the others tackle you and beat you repeatedly until you are dead.")
    elif choice == "punch":
        print "\nYou punch Rast in the throat. \nHe staggers back and collapses, gasping for air."
        print "Rast's acolytes look at their fallen, then at you. \nThey quickly stand at your side."
        print "Sam smiles and nods, mouthing \'thank you\' as Rast regains his breath."
        victory("The new recruits of Castle Black now respect you. \nIt's only smooth sailing from here...\n")
    elif choice == "stare down":
        print "\nYou face up to Rast and stare into his ugly, droolling mug."
        print "Rast smiles. Suddenly, a snowball hits you in the face, stunning you."
        dead("Rast and the others tackle you and beat you repeatedly until you are dead.\n")
    else:
        print "\nSorry, I do not understand. Try again!\n"
        rast_attack()



def kings_landing():
    print "\nNed: \"Son, I can't take you with me to King\'s Landing.\nNow that King Robert wants me to serve as Hand to the King, \nyour presence will only cause a stir and \nchallenge what little authority I will have there.\"\n"
    ned_stark_challenge()

def ned_stark_challenge():
    print "\nNed\'s words upset you to the core. You have three options:"
    print "- CHALLENGE Ned Stark to a \'Decision By Combat\'"
    print "- Respect Ned Stark\'s decision and HEAD NORTH to Castle Black"
    print "- Respect Ned Stark\'s decision and STAY PUT in Winterfell\n"

    choice = raw_input("> ")
    choice.lower()

    if choice == "challenge":
        ned_stark_combat()
    elif choice == "head north":
        castle_black_start()
    elif choice == "stay put":
        winterfell()
    else:
        print "\nSorry, I do not understand. Try again!\n"
        ned_stark_challenge()

def ned_stark_combat():
    print "\nNed is shocked that his own son would challenge him to a fight to the death."
    print "However, he is a man of the law and accepts your challenge."
    print "Which weapon do you choose: LONGCLAW, NEEDLE, or ICE?\n"

    choice = raw_input("> ")
    choice.lower()

    if choice == "longclaw":
        dead("\nA respectable choice, and after a mighty battle, you defeat Ned Stark. \nHowever, the victory is hollow, as you are cast out of the Stark family, \nnot to mention that the Seven Kingdoms is without a Hand, \nand all of Westeros descends into chaos.\n")
    elif choice == "needle":
        dead("\nA ridiculous choice. \nNed's massive Ice sword slices Needle in half.. and you as well.\n")
    elif choice == "ice":
        dead("\nYeah... that's Ned\'s sword. \nYou have no weapon and he quickly beheads you.\n")
    else:
        print "\nSorry, I do not understand. Try again!\n"
        ned_stark_combat()


def winterfell():
    print "\nOpting to stay in Winterfell, your stepmother CAT\'s general hostility \ntowards you only worsens. After your brother \nBrandon\'s crippling injury, Cat refuses to leave his side. \nShe also refuses to let you see him."
    print "Do you respect Cat\'s wishes and HEAD NORTH for Castle Black, \nor do you FORCE ENTRY into Brandon's room to see him?\n"

    choice = raw_input("> ")
    choice.lower()

    if choice == "head north":
        castle_black_arrival()
    elif choice == "force entry":
        print "\nCat: \"How dare you! GUARDS! SEIZE HIM!\""
        dead("\nWinterfell soldiers swarm you. \nYou put up a fight, but there are just too many. \nCat is the only Stark who does not weep at your funeral.\n")
    else:
        print "\nSorry, I do not understand. Try again!\n"
        ned_stark_combat()

def dead(why):
    print why, "Game over.\n"
    exit(0)

def victory(why):
    print why, "You win!\n"
    exit(0)

start()
