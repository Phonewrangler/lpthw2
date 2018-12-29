def cheese_and_crackers(cheese_count, boxes_of_crackers): #create the function
    print(f"You have {cheese_count} cheeses!") #and pass it two variables
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n") # write a paragraph and jump to a new line


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #pass the function data


print("Or, we can use variables from our script:")
amount_of_cheese = 10  #set up variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #pass variables to function


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) #do some math in the function


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#all the above
