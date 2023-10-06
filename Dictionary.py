# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate member

# Create dict
person = {
    'first_name': 'Fahad',
    'last_name': 'Sulaiman',
    'age': 25
}

# Use constructor
# person2 = dict(first_name='afeef', last_name='Sule')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '080-323-30375'

# Get dict keys
print(person.keys())

# Get  dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Hajjo', 'age': 10},
    {'name': 'ejjo', 'age': 11}
]

print(people[1]['name'])

