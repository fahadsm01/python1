# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in python is an object

# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1



# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and balance is {self.balance}'


# Init user object
fahd = User('Fahd', 'fahd@gmail.com', 25)
# Init customer object
mohd = Customer('mohd','mohd@gmail.com', 30)


mohd.set_balance(100)
print(mohd.greeting())


fahd .has_birthday()
print(fahd.greeting())