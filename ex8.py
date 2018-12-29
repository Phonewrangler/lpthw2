formatter = "{} {} {} {}" #define a variable as a 4 bracket string

print(formatter.format(1, 2, 3, 4))  #fills the brackets in the formatter string with 1 -4
print(formatter.format("one", "two", "three", "four")) # changes brackets to one - four
print(formatter.format(True, False, False, True)) #fills brackets with boolean true false statements
print(formatter.format(formatter, formatter, formatter, formatter)) #fills brackets with the original string
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
