#Print the numbers from 1 to 20
for twenty in range(1,21):
	print(twenty)
#Print a list of the numbers from one to a million
digits= range(1, 1_000_001)
for million in digits:
	print(million)
#Print the min, max, and sum of 1-1_000_001
print(min(digits))
print(max(digits))
print(sum(digits))
#print a list of odd numbers
odd_numbers= list(range(1, 21, 2))
print(odd_numbers)
#make a list of multiples of 3 from 3-30 and print the numbers
threes= list(range(3,31,3))
for multiple in threes:
	print(multiple)
#Print the first 10 cubes and print the value of each cube
cube= [value**3 for value in range(1,11)]
print(cube)