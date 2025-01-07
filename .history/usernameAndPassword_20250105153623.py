# Simple User Authenticator
# Build a python project that inputs username and password and later asks the user to enter them to validate it

print('### Authenticator App ###')
print('Create your account')
username = input('Enter username: ')
password = input('Enter password: ')

print('Account created for the User: ', username, 'successfully')

print('Login now!')
login_username = input('Enter username: ')
login_password = input('Enter password: ')

if login_username == username and login_password == password:
    print('User logged in successfully!')
else:
    print('Invalid credentials!')


