from sys import argv #imports the argv function from the sys library

script, filename = argv # unpacks the name of the script and the first
# command line argument from your entry

txt = open(filename) # sets the varaible txt = to the file in the command line
# and opens it for reading

print(f"Here's your file {filename}:") #displays the name of the txt filename
print(txt.read()) #prints out the contents of the text filename

print("Type the filename again:") #asks you to type the filename again for
#manual input
file_again = input(">")

txt_again = open(file_again) #opens the file using the new variable

print(txt_again.read()) #prints out the new variables contents

txt.close()
txt_again.close()
