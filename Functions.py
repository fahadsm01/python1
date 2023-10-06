# A funtion is a bloock of code which runs when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name='fahd'):
    print(f'Hello {name}')

# sayHello()

# Return values

def getSum(num1, num2):
    total = num1 + num2
    return total



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, But can only have one expression. very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))