#if-elif-else chain is usefule only if you need one test to pass
#use a series of 'if' statements when u want to check multiple condtions

requested_toppings= ['mushrooms', 'extra cheese']
#use 'in' when doing if statements w/ lists
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\n1. Finished making your pizza!\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#Use a loop to announce each topping as it's added to the pizza
for requested_topping in requested_toppings:
	#Ran pout of	 green peppers, so use an 'if' statement w/in the for loop
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		#If you do requested_toppings then the whole lists shows w/ []
		print(f"Adding {requested_topping}.")
print("\n2. Finished making your pizza!\n")

#Check whether the list of requested toppings is empty b4 building the pizza
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
else:
	print("3. Are you sure you want a plain pizza.\n")

#List of available toppings
available_toppings = ['mushrooms', 'olives', 'gren_peppers', 'pepperoni', 'pineapple', 'extra cheese']
#List of requested toppings
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we do not have {requested_topping}.")
print("\n4. Finished making your pizza!")
