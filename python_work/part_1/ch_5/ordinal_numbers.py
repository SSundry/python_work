#Store the numbers 1 through 9 in a list
numbers= [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(f"{numbers[0]}st")
	elif number == 2:
		print(f"{numbers[1]}nd")
	elif number == 3:
		print(f"{numbers[2]}rd")
	else:
		print(f"{number}th")