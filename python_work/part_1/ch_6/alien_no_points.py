alien_0 = {'color': 'green', 'speed': 'slow'}

#Use the get() method to set a default value if the requested key doesn't exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)