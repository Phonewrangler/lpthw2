#import some modules
from sys import exit


# Define the ascii art functions
def win_end():
    with open("ascii_woman.txt") as win:
        print(win.read())
        exit(0)

def start_art():
    with open("ascii_castle.txt") as castle:
        print(castle.read())

def lose_end():
    with open("ascii_skull.txt") as death:
        print(death.read())
        exit(0)


# Set up thefirst room
def main_room():
    print("\nYou enter a room with 3 doors.")
    print("There is one on the east, west, south, and north walls.")
    print("Which door do you go through?")

    door = input(">") #get the players choice

    #set up the branches
    if door == "east":
        east_room()
    elif door == "west":
        west_room()
    elif door == "north":
        north_room()
    elif door == "south":
        south_room()
    else: #consequences
        print("Not chosing is a choice in itself")
        print("You are struck by a bolt of lightning and die")
        lose_end()


#create the east room
def east_room():
    print("You enter a room full of spider webs")
    print("What do you do?")
    print("1. Burn the webs out with a torch")
    print("2. Hack at the webs with you sword.")
    print("3. Back out and shut the door")

    spider = input(">") #get the players choice

    if spider == "1":
        print("""The burning webs ignite some kegs of gunpowder
        and you are turned into little chunks!""")
        lose_end()
    elif spider == "2":
        print("You are eaten by a giant spider!")
        lose_end()
    elif spider == "3":
        print("That was probably a wise choice.")
        main_room()
        door = input(">")

    else:
        print("Not the sharpest tack are we?")
        main_room()

#create the west room
def west_room():
    print("You see a manticore!")
    print("What's your plan?")
    print("1. Fling a booger at it")
    print("2. Flash you buttocks")
    print("3. slowly back out and shut the door")

#completely unnecessary use of extra code just to test some new knowledge
    while True:
        try:#will test input to see if integer
            manticore = int(input(">")) #get the players choice and convert to integer
            break #stop loop
        except ValueError: # cause an exception if input is of the wrong type
            print("Enter a number dummy")
#inputs were converted to integers in last block
    if manticore == 1 or manticore == 2:
        print("You're a special kind of stupid aren't ya?")
        lose_end()
    elif manticore == 3:
        print("Good plan")
        main_room()


    else:
        print("I can't believe you still haven't got how this works")
        main_room()

#create the north room
def north_room():
    print("There is a writhing tentacle growing from the floor")
    print("How do you want to play this?")
    print("1. attack")
    print("2. Try to walk around it.")
    print("3. run for the hills")


    tent = input(">") #get the players choice

    if tent =="1":
        print("Your sword bounces off the rubbery flesh and decapites you")
        lose_end()
    elif tent == "2":
        print("The tentacle lashed out and smashes you")
        lose_end()
    elif tent == "3":
        print("Your kind of running out of doors")
        main_room()

    elif tent == ("sexy"):
        print("""You find something very sexy about the tentacle.
        You slowly approach and disrobe.
        As you get near the tentacle wraps around your leg and slowly inserts
        itself into your nether orifice. After several orgasms a beautiful
        woman approachs. She tells you that this is her castle and she's been
        waiting for a suitable consort for her and her favorite pet. She asks
        you to stay with her and help rule the kingdom.""")
        win_end()


#create the south room
def south_room():
    item = 'whip', 'phallus', 'chain'
    print("There are several strange golden items on a shelf in this room")
    print("There's a whip, a large phallus, and a chain")
    print("Under the shelf is a sign, which says 'Take one'.")
    print("Which one do you take?")
    instrument = input(">") #get the players choice

    if instrument == item[0]:
        print("You are killed by a Balrog!")
        lose_end()
    elif instrument == item[2]:
        print("You are killed by Ghost Rider!")
        lose_end()
    elif instrument == item[1]:
        print("A large minotaur bursts into the room and fucks you to death!")
        lose_end()
    else:
        print("You wisely choose nothing")
        main_room()



print("You come upon a castle in the woods")
start_art()
print("Do you enter?")

adventure = input(">") #get the players choice

if adventure == "no":
    print("Loser!")
    lose_end()
elif adventure == "yes":
    main_room()
else:
    print("Can you not figure out how this works?")
    main_room()



game_over()
