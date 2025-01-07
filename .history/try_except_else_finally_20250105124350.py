try:
    num = int(input('Enter an integer: '))
    print('The integer is' , num)
except TypeError:
    print('There is a Type error')
except:
    print('Something went wrong')
else:
    print('All good. No errors')
finally:
    print('Try Except completed')

'''
SyntaxError: if the syntax is incorrect like missing a ":"
NameError: A variable is not defined
TypeError: A type error like trying to concatenate an integer
IndexError: If the list index is out of range
AttributeError: If the attribute of a method or an object does not exist
Logical Errors: In the logic is incorrect
'''

# More Errors and details can be found here
# https://docs.python.org/3/library/exceptions.html#inheriting-from-built-in-exceptions