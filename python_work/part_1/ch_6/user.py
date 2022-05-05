#Create a dictionary that store one person's username, first name and last name:
user_0 = {
	'username': 'enfermi',
	'first': 'enrico',
	'last': 'fermi',
}

#Create a for loop to see everything stored in the dictionary
# .items() returns a list of k-v pairs
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")
#shorthand version is --> for k, v in user_0.ite