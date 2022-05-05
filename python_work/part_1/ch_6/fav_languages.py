#It's good practice to include a comma after the last k-v pair
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

#To see which language Sarah chose, we ask for the value at:
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

#Loop to get the name of each person and their fav programming lang
# .items() returns a list
for k, v in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
