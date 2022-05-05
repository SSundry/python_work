#Create a dictionary w/ 2 key-value pair
#A key-value pair is a set of values associates w/ each other through a colon
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
#Add 2 more key-value pairs
#How to add a k-v pair: give the name of the dict. followed by the new key in [] along w/ the new value. 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Fill an empty dictionary
alien_1 = {}
alien_1['color'] ='yellow'
alien_1['points'] = 10
print(alien_1)

#Modify a value in a dictionary
print(f"The alien is {alien_1['color']}.")
alien_1['color'] = 'purple'
print(f"The alien is now {alien_1['color']}.")

#Track the position of an alien that can move at dif. speeds
alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")

#Change the new position to 3
alien_0['speed'] = 'fast'

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3

#The new position iis the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']} ")

#Removing k-v pairs
print(alien_0)

del alien_0['points']
print(alien_0)