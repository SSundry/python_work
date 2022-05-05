#Make a list of at least five places you want to visit in the world
travel_locations= ['tokyo', 'paris', 'manchester', 'toronto', 'seattle', 'madrid', 'taipei']
print(travel_locations)
#Print the list in alphabetical order w/o modifying the actual list
print('\nThis is the list in alphabetical order')
print(sorted(travel_locations))
#print the original list
print('\nAnd this is the original list')
print(travel_locations)
#Print the list in reverse alphabetical order
print('This is the reverse alphabetical order')
#.reverse() prints 'None' b/c the fcn doesn't return a new objecct since it uses a modified list
#use sorted(variable, reverse=True) to create a reverse alphabetical order
print(sorted(travel_locations, reverse=True))
#print original list
print(travel_locations)
#reverse the order of the list and print to show the change
travel_locations.reverse()
print(travel_locations)
#reverse it back again adn print to show the original order
travel_locations.reverse()
print(travel_locations)
#Change your list permanently to alphabetical order
#if you do print(travel_locations.sort()) it'll print None
travel_locations.sort()
print(travel_locations)
#Reverse the alphabetical order
travel_locations.reverse()
print(travel_locations)