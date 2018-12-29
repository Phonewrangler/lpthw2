from sys import exit

def gold_room(): #create the prize room
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice: #determine if answer is a number
        how_much = int(choice)
    else:
        dead("Man learn to type a number.")

    if how_much <= 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!") #call the dead function and pass the cause


def bear_room(): #create the bear room
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">") #get the bear away from the door to the gold room

        if choice == "Take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I've no idea what that means.")


def cthulu_room(): #create the cthulu room
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice: #go back to beginning
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()


def dead(why): #create dead function and leave an opening for the cause
    print(why, "Good job!")
    exit(0)

def start(): #create the beginning of the game
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start() #begin the game
