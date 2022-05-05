#Copy a list
my_foods= ['pizza', 'falafel', 'carrot cake']
#The slice that includes the entire originaal list by omitting the first and second indexes
friend_foods= my_foods[:]
#Proves that two separate lists have been created
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)
# if you set friend_foods and my_foods equal to each other  then you would create two of the same list

print("\nMy favorite foods are:")
for my_food in my_foods:
	print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
	print(friend_food)

