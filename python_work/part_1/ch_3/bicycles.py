#A list is a collection if items in a particular order.
#In python []indicates a list and individual elements in the list are separated by commas
bicycles = ['trek','cannondale','redline', 'specialized']
#Will print the entire list including the []
print(bicycles)

#Since lists are ordered collections you can access any element in a list by telling Python the index(position) of the the item desired
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[3])
#Python always returns the last item in the list if you ask for index -1
print(bicycles[-1])

#\n is always w/in quotes
message = f"\nThe first bicycle I've ever rode was a {(bicycles[1].title())}."
print(message)
