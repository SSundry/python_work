#Print a list the first 10 square numbers
#create a variable with an empty list
squares =[]
#Loop through each value from 1-10
for value in range(1,13):
	# ** represents exponents
	#inside the loop, raise  the current value to the 2nd power and assign it to a new variable
	square= value ** 2
	#Add the new values to the empty list
	squares.append(square)
#Print the list of squared numbers
print(squares)

#A more concise way
squares_1= []
for value_1 in range(1,14):
	squares_1.append(value_1 ** 2)
print(squares_1)

#Create a list comprehension:This means generating the same list all in one line of code
#squares_2 is the descriptive names for the list; in the [] define the expression for the values which is value_2**2 which will raise the value to the 2nd power; write the for loop. NO COLON IS NEEDED
squares_2= [value_2**2 for value_2 in range(1,15)]
print(squares_2)

#Print the min, max and sum of a list of numbers
#Replacing the numbers with the range method causes an errot
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
