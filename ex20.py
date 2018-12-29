from sys import argv # import argv function

script, input_file = argv #unpack argv

def print_all(f): # create a function that prints out the current file
    print(f.read())

def rewind(f): #create a function that goes back to beginning of file
    f.seek(0)

def print_a_line(line_count,f): #create a function that prints out a specific line
    print(line_count, f.readline())

current_file = open(input_file) #define a variable

print("First let's print the whole file: \n")

print_all(current_file) #call a function on the variable

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #go back to beginning of file

print("Let's print three lines:")

current_line = 1 # define a variable
print_a_line(current_line, current_file)

current_line += 1 #add 1 to current line
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
