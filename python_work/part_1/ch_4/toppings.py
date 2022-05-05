# '!=' represents not and determines whether two values are not equal
requested_topping= ['mushrooms', 'onions' 'pineapple']
#Print a message if the person did not order anchovies
if requested_topping != 'anchovies':
	print("Hold the anchovies!\n")

#'in' lets you find out whether a specific value is already on the list
print('mushrooms' in requested_topping)
#True

print('pepperoni' in requested_topping)
#False