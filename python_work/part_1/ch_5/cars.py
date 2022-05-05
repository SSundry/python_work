#A simple example
cars= ['audi', 'bmw', 'subaru', 'toyota\n']
for car in cars:
	#'==' checks whether the value of car is 'bmw and returns True us the values match and False if they don't
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

		
car ='Audi'
print(car== 'audi')
#False b/c when checking for equality IS case-sensitive

car= 'Audi'
print(car.lower()== 'audi')
#True because the test is now case insensitive