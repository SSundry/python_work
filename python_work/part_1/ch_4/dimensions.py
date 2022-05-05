#Tuples are lists that cannot change AKA they are immutable
#A tuple is defined by using () and COMMA instead of []
dimensions= (200, 50)
#You can loop tuples too!
for dimension in dimensions:
	print(dimension)

#dimensions[0]= 250 would not work because tuples are immutable

#To define a tuple with one element, you need to add a trailing COMMA
my_t= (3,)

#You can redefine/assign a new value to the variable that represents a tuple
print('\nOriginal dimension:')
for dimension in dimensions:
	print(dimension)
#The reassignment of the variable is valid
dimensions=(400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)