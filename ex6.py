types_of_people = 10 #defines variable
x = f"There are {types_of_people} types of people." #defines a variable = to a
# string with a nested variable.

binary = "binary" #defines a variable
do_not = "don't" #defines a variable
y = f"Those who know {binary} and those who {do_not}." #another string with 2
#nested variables

print(x) #print the variable with nested variable
print(y) #ditto

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #defines a variable with an empty
# variable

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
