try:
    num = int(input('Enter an integer: '))
    print('The integer is', num)
except:
    print('Something went wrong')
else:
    print('All good. No errors')
finally:
    print('Try Except completed')

