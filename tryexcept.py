# Using try/except to anticipate possible code breaking/user error and avoid a traceback error
favNum = 'Derrick'
try:
        istr = int(favNum)
except:
        istr = 7

print('Fav. Number: ', istr)

# Resetting favNum and doing another try/except clause
favNum = '11'
try:
        istr = int(favNum)
except:
        istr = 0

print('Fav. Number now: ', istr)

# Real-world example that is based on user input
birthYear = input('Enter your birthyear: ')
try:
        inp = int(birthYear)
except:
        inp = 1900

if (inp > 1900):
        print('Your birthyear is', inp, 'which makes you ~', 2021 - inp, 'years old')
else:
        print('Invalid input!')