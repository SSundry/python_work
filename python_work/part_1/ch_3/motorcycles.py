motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifies elements in a list
motorcycles[0] ='ducati'
print(motorcycles)

#adds elements to the end of a list
motorcycles.append('kawasaki')
print(motorcycles)

motorcycles_1 = []
motorcycles_1.append('KTM')
motorcycles_1.append("Aprilia")
motorcycles_1.append('kawasaki'.title())
print(motorcycles_1)

#adds elements to the beginning of a list
motorcycles_1.insert(0, 'bmw'.upper())
print(motorcycles_1)

#removes elements from the list
del motorcycles[0]
print(motorcycles)

#pop() method removes the last item in a list, but alllows you to still use it. 
motorcycles_2= ['yamaha', 'vespa', 'bimota', 'piaggo']
last_owned= motorcycles_2.pop()
print(motorcycles_2)
#The value 'piaggo' has been removed form the end of the list and now assigned to a new variable
print(last_owned)
#remember that each time the pop() method is used, the item you work with is no longer stored in the list
print(f"\nThe last motorcyle I owned was a {last_owned.title()}.")
#pops the first item in the index
first_owned=motorcycles_2.pop(0)
print(f"The fist motorcycle I owned was a {first_owned.title()}.\n")

#If you want to delete an item from a list and not use the item in any way use the 'de1' statement; if you want to use an item as you remove it, use the pop() method

print(motorcycles)
#use remove() if you don't know the position of the value you want to remove from a list
motorcycles.remove('suzuki')
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
#the value of a variable is a string so use quotes
too_expensive= 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive.upper()} is too expensive for me")

#index errors
#"IndexError: list index is out of range" means that python cannot find an item at the inder you've requested or the list is empty.
print(motorcycles[3])