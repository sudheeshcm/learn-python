# Calculator
# A function to accept 3 inputs from the user. The first 2 arguments are numbers and the 3rd is an operator

num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))
operator = input('Enter the operator:')

print('Number 1:', num1, '\nOperator:', operator, '\nNumber 2:', num2)

if operator == '+':
    print('Sum: ', num1+num2)
elif operator == '-':
    print('Difference: ', num1 - num2)
elif operator == '*':
    print('Product: ', num1 * num2)
elif operator == '/':
    print('Quotient: ', num1 / num2)
elif operator == '%':
    print('Reminder: ', num1 % num2)
else:
    print('Operator not found!')