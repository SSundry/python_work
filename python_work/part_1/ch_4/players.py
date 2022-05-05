#Make a list of players on a team
players= ['adebayo', 'peacemaker', 'vigilante', 'harcourt','murn']
#Slice the list, it is similar to the range() fcn , so 0:3 returns the elements 0, 1, 2.
print(players[0:3])
print(players[1:4])
#Omitting the first index in a slice will make Python automatically start the slice at the beginning
#The COLON is important, or it will just pick out one name
print(players[:4])
#Omitting the second index  will show the items all the way till the end
print(players[2:])
#Output the last players on the roster
print(players[-3:])
#Loop through the first three players and print ther names
message= "\nHere are the first three [;ayers on my team"
print(message)
for player in players[:3]:
	print(player.title())