#create a list
fav_foods=['waffles','avocado toast','fried egg', 'oxtail', 'jollof rice', 'fufu & soup', 'popcorn']

#Make three messages
message_1= "\nThe first three items in the lists are:"
message_2= "\nThree items from the middle of the list are:"
message_3= "\nThe last three items in the list are:"

#Use a slice to print the first 3 items
print(message_1)
#Must print something when using for loop
#to choose the forst 3 items the number goes after the COLON
for fav_food in fav_foods[:3]:
	print(fav_food.lower())

#Use slice to print the 3 middle items
print(message_2)
#Python stops at index 5, so it doesn't print out the fourth item
for fav_food in fav_foods[2:5]:
	print(fav_food.lower())

#Use slice to print the last 3 items
print(message_3)
#to choose last items the number goes before the COLON
#-3  chooses the the items thhat is in last place which is also -1and goes backwards
for fav_food in fav_foods[-3:]:
	print(fav_food.lower())
