#Make a list of different kinds of pizzas
pizzas= ['pepperoni', 'hawaiian', 'cheese']
#Print the name of each pizza
for pizza in pizzas:
	print(f"I like {pizza} pizza!")
#Add ONE more additional sentence
message= f"However, I like {pizzas[0]} pizza the most.\n"
print(message)
#Make a list o different animals  with common characteristics
animals= ['newt', 'frog', 'turtle']
for animal in animals:
	print(f"A {animal} would make a great pet.")
print("All of these animals are amphibious!")
#Copy the list and name is friend_pizzas
friend_pizzas= pizzas[:]
#Add another type of pizza to the original list
#If you add and print the list b4 copying it then the frinds_list will have both sausage and veggie
pizzas.append('sausage')
print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
#Add a dif. type of pizza to the friend's list
friend_pizzas.append('veggie')
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)