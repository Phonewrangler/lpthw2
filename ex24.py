print("Let's practice everthing.") #print out line
print('You\'d need to know \'bout escapes with \\ that do:') #line with escapes
print('\n newlines and \t tabs.') # more escapes
#def variable poem on multiple lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("---------------")
print(poem) #print out the poem
print("---------------")


five = 10-2+3-6 #do a math prob that equals 5
print(f"This should be five:{five}") #print line with total from prev problem

def secret_formula(started): #define the function secret formula include argument started
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000 #def startpoint and call function with variable
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of:{}".format(start_point))
# It's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))