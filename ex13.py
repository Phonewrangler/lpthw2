from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

name = input("What is your name? ")
print(f"Well, {name}")
print("What do we like? ", first)
print("How do we like them? ", second)
print("In what shape? ", third)
