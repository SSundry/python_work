car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#True b/c the variable is now capital S
print("\nIs car == 'Subaru'? I predict False.")
print(car.title() == 'Subaru')

fav_book = 'crooked kingdom'
print(f"\nIs fav_book == {fav_book.title()}? I predict True.")
print(fav_book == 'crooked kingdom')

print("\nIs fav_book == 'The Last Thing He Told Me?' I predict False.")
print(fav_book == 'The Last Thing He Told Me')

coke_product = 'sprite'
print(f"\n Is coke_product == {coke_product.title()}? I predict True.")
print(coke_product == "sprite")

print("\n Is coke_product == 7UP? I predict False.")
print(coke_product == "7UP")

drink = 'kombucha'
print('\nIs favorite healthy drink == kombucha? I predict True.')
print(drink == 'kombucha')

print('Is favorite healthy drink == sprite. I predict False.')
print(drink == 'sprite')

#Test for equality and inequality with strings
if drink != 'sprite':
	print('\nCan I have sprite as my drink?')
if drink == 'kombucha':
	print(f"Actually, can I have {drink.upper()} instead?\n")

#Numerical test using the NOT sign
answer= 10
if answer != 15:
	print("The answer is 10 NOT 15!\n")

#Numerical test using the keyword 'or' and 'and'
fav_num_1= 3
fav_num_2= 9
print(fav_num_1 >= 21 or fav_num_2 <= 21)
print(fav_num_1 >= 21 and fav_num_2 <= 21)

#Test whether an item is in a list
cars= ['subaru', 'audi', 'toyota', 'bmw']
message= cars[-1] in cars
print(message)
#Test whether an item is NOT in a list
electric_car= 'tesla'
if electric_car not in cars:
	print(f"{electric_car.title()} is an electric car. Please pick another car.")