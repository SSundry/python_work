#To test more than two possible situations, use Python's if-elif-else syntax
#Print the different rates for anyone under age 4, b/t 4 and 18, and 18 or older.
age = 12
#the 'if' tests whether the person is under 4yrs old. Python skips this one
if age < 4:
	price = 0
#the 'elif' tests  if the person is under 18. Python prints the message and stops b4 the 'else' block
elif age < 18:
	price = 25
#multiple 'elif' tests can be used
elif age < 65:
	price = 40

#if the 'elif' tests fail then Python will run the 'else' block
#else:
	#price = 20

#an 'else' block is not required in Python
#If the person is 65 or older the admission price is $20
elif age >= 65:
	price = 20
print(f"Your admission cost will be ${price}.")