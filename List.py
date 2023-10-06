# A List is a collection which is ordered and changeable. Allows duplicate member

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Oranges', 'Grape', 'Pears']
# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get Value
print(fruits[1])

# Get Length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grape')

# Insert into position
fruits.insert(2, 'strawberries')

# Change value
fruits[0] = 'blueberries'

# Remove with pop
fruits.pop(2) 

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

