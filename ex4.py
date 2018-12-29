cars = 100 #assigns a value to variable "cars"
space_in_a_car = 4.0 #define the number of people that can fit in a car
drivers = 30 #gives us the number of drivers
passengers = 90 #how many passengers need transport
cars_not_driven = cars - drivers #defines how many cars have matched drivers
cars_driven = drivers #gives an alias for cars_driven
carpool_capacity = cars_driven * space_in_a_car #defines how many people can
#get a ride
average_passengers_per_car = passengers / cars_driven ##how many people need to
#be stuffed in each car


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
