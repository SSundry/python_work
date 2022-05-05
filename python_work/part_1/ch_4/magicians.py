#Use a for loop to print out each name (you won't see the list in [])
#make a list
magicians= ['nneka', 'alice', 'caroline']
#magician is a temporary variable that will be associated with each value in the list. Choose a meaningful name that represtes a single item from the list
for magician in magicians:
	#in a for loop print needs to be indented to be considered 'inside the loop'
	print(f'{magician.title()}, that was a great trick!')
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
#This is outside of the loop, so it'll be executed only once. So use this as a way to summarize an operation that was performeson an entire data set. 
print("Thank you, everyone. That waaas a great magic show!")
