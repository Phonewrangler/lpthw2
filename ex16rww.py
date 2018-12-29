from sys import argv

script, filename = argv #unpack argv

print(f"We're going to erase {filename}.") #tell user whats going to happen to which file
print("If you don't want that, hit CTRL_C (^C).") #give user a chance to stop
print("If you do want that, hit RETURN.")

input("?") #wait for user to opt in

print("Opening the file...")
target = open(filename,'w') #open the file and set to target

print("Truncating the file. Goodbye!")
target.truncate() #erase the contents of target

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:") #get the new lines for the file
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}") # writes the new lines to the file in a list

print("And finally, we close it.")
target.close() #close the file
