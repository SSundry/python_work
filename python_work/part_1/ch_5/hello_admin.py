#Make a list of at least 5 usernames
usernames= ['admin', 'ran', 'miki', 'su', 'diamond']
#Print a greeting to each user and a special greeting for admin
for username in usernames:
	if username == "admin":
		print("1. Hello admin, would you like to see a status report?")
	else:
		#Use the singular noun variable to list the names one by one
		#Use the plural noun variable to show the whole list
		print(f"Hello {username.title()}, thank you for logging in again.")
	
usernames= []
#Have a message if there is an empty list
#Check if the list is empty b4 using the for loop
if username:
	for username in usernames:
		print(f"Hello {username.title()}, thank you for logging in again.")
	else:
		print("2. We need to find some users!")

#Make a list of 5 or more usernames
current_users= ['yuSUke', 'kuwabara', 'kurama', 'Hiei', 'bOtan', 'Genkai', 'keiko']
#Make a list called new_users that has at least one from the other list
new_users= ['hiei', 'genKAI', 'GON', 'kurapika', 'LeOrio', 'KILLUA']
#Make list comprehensions of the two lists containg lowercase versions of all existing users
current_users= [username.lower() for username in current_users]
new_users= [username.lower() for username in new_users]
for username in new_users:
	if username in current_users:
		print(f"\nThe username, {username}, is already taken. Please input a new username.")
	else:
		print(f"\nWelcome, {username}!")