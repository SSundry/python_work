#The cars are now in alphabetical order, and we can never revert to the original orger
#the sort() function modifies the actial list
cars= ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#you can reverse the order through passing this method
cars.sort(reverse=True)
print(cars)

#the sorted() unction ceats  new list with the modified elements, so the original elements are not affected
cars_2=['mercedes', 'tesla', 'ford', 'honda']
print("Here is the original list:")
print(cars_2)

print("\nHere is the sorted list:")
print(sorted(cars_2))

print("\nHere is the original list again:")
print(cars_2)

print('\n')

print(cars)
#prints in reverse order
cars.reverse()
print(cars)

print('\n')
#can find out the length of a list by using the len()function. You can see it if you do print()
print(len(cars))