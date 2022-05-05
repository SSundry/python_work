#print a series of numbers
for value in range(1,5):
	#Will print out 1-4 because python stops at the 2nd value given (5), so the output never contains the end value
	print(value)
#If you pass range() only one argument it'll starts from 0 and still stops right before, not containing the end value
for value in range(6):
	print(value)
#print a list of numbers
numbers= list(range(1,6))
print(numbers)
#Print a list of even numbers
#the range() fcn starts with the value 3 and then adds 2 to that value  until it reaches the end value, 11 (so it stops at 10)
even_numbers= list(range(2,11,2))
print(even_numbers)