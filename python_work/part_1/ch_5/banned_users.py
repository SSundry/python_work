banned_users= ['andrew', 'carolina', 'david']
user= 'marie'

#'not' checks if a value does NOT appear in a list
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

	#Boolean Expressions
	#Boolean value is either Ture or False
	game_active = True
	can_edit = False