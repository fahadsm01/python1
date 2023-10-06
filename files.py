# Python has functions for creating, updating, and deleting files.

# Open a file
myfile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myfile.name)
print('Is Closed: ', myfile.closed)
print('Opening Mode: ', myfile.mode)

# Write to file
myfile.write('I love python')
myfile.write(' and JavaScript')
myfile.close()

# Append to file
myfile = open('myfile.txt', 'a')
myfile.write(' and I also like PHP')

# Read from file
myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
print(text)