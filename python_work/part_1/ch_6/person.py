person = {
	'first_name': 'feitan',
	'last_name': 'portor',
	'age': 'unknown',
	'city': 'meteor city',
}
first_name = person['first_name'].title()
last_name = person['last_name'].title()

#Each variable has its own {}
print(f"My name is {first_name} {last_name}...")
print(f"My age is {person['age']} and I do not even know my birthday.")
print(f"I am from {person['city'].title()}...")