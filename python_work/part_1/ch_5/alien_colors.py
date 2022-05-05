#Create  variable and give it an RGB value
alien_color= ['green', 'red', 'yellow']
#Needs to be points_5 becuz Python CANNOT start a number
points_5 = "You've earned 5 points.\n"
points_10 = "You've earned 10 points.\n"
points_15 = ""
#Write an if statement and print message that the player earned 5pts
if 'green' in alien_color:
	print(points_5)
elif 'yellow' in alien_color:
	print(points_10)
else:
	print(points_10)

alien_color_1= ['purple', 'blue', 'orange']
if 'green' in alien_color_1:
	print(points_5)
else:
	print(points_10)