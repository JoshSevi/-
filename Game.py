import sys
import os
import time
screen_width = 100

################
# Player Setup #
################
class player:
    def __init__(self):
        self.name = ''
        self.memories = ''
        self.age = ''
        self.origin = ''
player1 = player()


################
# Title Screen #
################
def title_screen_options():
    #Allows the player to select the menu options, case-insensitive.
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("help"):
        help_menu()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Invalid command, please try again.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("quit"):
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()

def title_screen():
    #Clears the terminal of prior code for a properly formatted title screen.
    os.system('clear')
    #Prints the pretty title.
    print('#' * 45)
    print('# Welcome to this text-based puzzle RPG for #')
    print("#      Bryan Tong's CS10 Final Project!     #")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


#############
# Help Menu #
#############
def help_menu():
    print("")
    print('#' * 45)
    print("Written by Bryan Tong")
    print("Version Final (1.0.2a)")
    print("~" * 45)
    print("Type a command such as 'move' then 'left'")
    print("to nagivate the map of the cube puzzle.\n")
    print("Inputs such as 'look' or 'examine' will")
    print("let you interact with puzzles in rooms.\n")
    print("Puzzles will require various input and ")
    print("possibly answers from outside knowledge.\n")
    print("Please ensure to type in lowercase for ease.\n")
    print('#' * 45)
    print("\n")
    print('#' * 45)
    print("    Please select an option to continue.     ")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


#################
# Game Handling #
#################
quitgame = 'quit'

################
# Execute Game #
################
def setup_game():
    #Clears the terminal for the game to start.
    global age_string
    os.system('clear')

    # Establishes introduction
    speech1 = "The lights flicker\n"
    speech2 = "The curtains rise on your legend\n"
    speech3 = "I wonder what role you will play?\n"
    speech4 = "No matter.\n"
    speech5 = "The only important thing now is...\n"
    speech6 = "...your name\n"


    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1)

    #QUESTION NAME: Obtains the player's name.
    question1 = "Enter your name here: "
    for character in question1:
        #This will occur throughout the intro code.  It allows the string to be typed gradually - like a typerwriter effect.
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(" ")
    player1.name = player_name

    speech7 = player1.name + "? Why does it sound familiar....\n"
    speech8 = "Now...\n"
    speech9 = "Your world...\n"

    for character in speech7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in speech8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in speech9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)

    #QUESTION MEMORIES: Obtains the player's memories.
    question2 = "Do you remember it?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    memories = input("> ")
    player1.memories = memories.lower()

    #Creates the adjective vocabulary for the player's memories.
    yes_memories = ['y', 'yes', 'yah', 'yup']
    no_memories = ['idk', 'n', 'no', 'nah']

    #Identifies what type of memories the player is having and gives a related-sounding string.
    if player1.memories in yes_memories:
        memories_string = "Good. That'll make it easier for me."
    elif player1.memories in no_memories:
        memories_string = "No? Hehehe. You really are troublesome right up to the very end, aren't you?"
        question33 = memories_string + ".\n"
        for character in question33:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        memories_string = "As I suspected... You don't seem to be the true owner of this story. Goodbye."
        question44 = "Well then, " + player1.name + ", " + memories_string + "."
        for character in question44:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        quit()

    while memories.lower() in no_memories:
        question55 = "Do you even want to remember?\n"
        for character in question55:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        memories = input("> ")
        player1.memories = memories.lower()

        if player1.memories in yes_memories:
            memories_string = "Good. That'll make it easier for me."
        elif player1.memories in no_memories:
            memories_string = "As if I care. I have a job to do y'know? It'll all come to you soon."
            print("Well then, " + player1.name + ", " + memories_string + ".")
            quit()
        else:
            memories_string = "As I suspected... You don't seem to be the true owner of this story. Goodbye."
            print("Well then, " + player1.name + ", " + memories_string + ".")
            quit()



    #Combines all the above parts.
    question3 = "Well then, " + player1.name + ", " + memories_string + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

    os.system('clear')
    # REALIZATION

    speech10 = "As per 死神 and librarian guidelines, I will help you remember your story.\n"
    speech11 = "Firstly, I need you to remember who you were.\n"

    for character in speech10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)


    #QUESTION AGE: Obtains the player's age.
    question4 = "Young, Adult, or Elderly?\n"
    for character in question4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    age = input("> ")
    acceptable_age = ['young', 'adult', 'elderly']
    #Forces the player to write an acceptable age.

    while age.lower() not in acceptable_age:
        print("That is not an acceptable sign, please try again.")
        age = input("> ")
    player1.age = age.lower()

    if player1.age == 'young':
        age_string = "Ah... whether you were fortunate or not... To know this story came from a child... I'm sorry"
    elif player1.age == 'adult':
        age_string = "So your story began at the height of your life? How lucky of you"
    elif player1.age == 'elderly':
        age_string = "Fate chose you, regardless of age. Your strength might have waned but your wisdom was greater than ever"

    question5 = age_string + ".\n"
    for character in question5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    playerorigin()

def playerorigin():
    global origin_string
    speech12 = "Now, do you remember where you came from?\n"
    speech13 = "According to our data, there are only three settlements you could've possibly hailed from.\n"
    speech14 = "Was it Riverrun? A quaint and homely town; far from conflict and disaster with kind and happy folks.\n"
    speech15 = "Was it Aega? A citadel city, standing between order and chaos. Its citizens are hardy and courageous.\n"
    speech16 = "Hm...\n"
    speech17 = "Ah!\n"
    speech18 = "Apologies, I had almost forgotten about Lunaly. That hidden settlement deep in the Aelvic woods.\n"
    speech19 = "I've heard that its citizens are wise and knowledgeable beyond their years.\n"
    speech20 = "Could it be an academic's paradise?\n"
    speech21 = "Now, pray tell where you hailed from.\n"
    for character in speech12, speech13, speech17, :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    for character in speech15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in speech16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech18:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech19:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech20:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech21:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

    # QUESTION ORGIN: Obtains the player's origin.
    question6 = "Riverrun? Aega? Lunaly? or could you possibly hail from... nowhere?"
    for character in question6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    origin = input("> ")
    acceptable_origin = ['riverrun', 'aega', 'lunaly', 'nowhere']
    # Forces the player to write an acceptable age.

    while origin.lower() not in acceptable_origin:
        print("That is not an acceptable origin, please try again.")
        origin = input("> ")
    player1.origin = origin.lower()




    if player1.origin == 'riverrun':
        origin_string = "Riverrun? How envious. Everyone else I've talked to so far came far more troubled backgrounds."
    elif player1.origin == 'aega':
        origin_string = "I see. Born in the face of adversity and chaos. You must be strong..."
    elif player1.origin == 'lunaly':
        origin_string = "Oh! I haven't met someone from there for quite some time. The last one was 200 years ago... Anyways."
    elif player1.origin == 'nowhere':
        # IF PLAYER INPUT NOWHERE
        speech22 = "...I...\n"
        speech23 = "...Let's move on.\n"
        origin_string = "Ah... A fellow orphan...? I understand your plight all too well.\n" + speech22 + speech23


    question7 = origin_string + ".\n"
    for character in question7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

    os.system('clear')
    goodbye()

def goodbye():
    speech24 = "It seems we are finished.\n"
    speech25 = "For the sake of guidelines, I must ask you to repeat what you have said to me\n"
    speech26 = "I will repeat what you have told me.\n"
    speech27 = "You are " + player1.name + ", " + player1.age + ", " + player1.origin + ".\n"
    speech28 = "I thank you for your cooperation.\n"
    speech29 = "May you find you worth, in the last reenactment of your story.\n"

    for character in speech24:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech25:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech26:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech27:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech28:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    for character in speech29:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

title_screen()