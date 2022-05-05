#Write an if-elif-else chain that determines a person's stage of life.
age = 23
person = [2, 4, 13, 20, 65]
if age < person[0]:
	#
	life = "baby"
elif age < person[1]:
	life = "toddler"
elif age < person[2]:
	life = "kid"
elif age < person[-2]:
	life = "teenager"
elif age < person[-1]:
	life = "adult"
else:
	life = "elder"
print(f"The person is a(n) {life}.")