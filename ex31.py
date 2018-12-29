print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There is a giant bear eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("the bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Bluberries")
    print("2. Yellow Jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "69":
    print("""You see a naked lady
    Do you:""")
    print("1. Say Hi and back out of the room")
    print("2. Come on strong")
    print("3. Get naked")

    succubus = input(">")
    if succubus == "1":
        print("Never trust a naked lady")
    elif succubus == "2":
        print("Congatulations! You just added to her dried husk collection")
    elif succubus == "3":
        print("Bow chika bow wow")
    else:
        print("Prepare for an ass raping!")




else:
    print("You stumble around and fall on a knife and die. Good Job!")
