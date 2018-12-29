#title section
print("A resistor divider calculator")

#input section
print("What's your input voltage?")
#gets the volts in value and converts the string to an integer
vin = int(input("V="))
print("What is the value of resistor 1 in ohms?")
#gets the value of the 1st resistor and prompts with an ohm
r1 = int(input("\u03a9 = "))
print("What is the value of the second resistor?")
#gets the value of the 2nd resistor and prompts with an ohm
r2 = int(input("\u03a9 = "))

#math section
#works the calculation and sets the answer equal to the variable vout
vout = vin * r2 / (r1+r2)

print(f"The output would be {vout} volts") #prints the output
