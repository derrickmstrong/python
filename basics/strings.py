fruit = 'banana'

# Get length of string
fruit_length = len(fruit)
print(fruit_length)

# Look through letters in string
for letter in fruit:
    print(letter)

# Loop through string and count num of a's in fruit variable
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
print("Number of a's in", fruit, count)

# Slicing
str = 'Monty Python'
print(str[0:4]) # Slice chars 0 up to but not including position 4 so 0-3
print(str[3:4]) # Slice char 3 but not including 4 so only 3
print(str[:2]) # Slice char 0 up to but not including 2 so only 0-1
print(str[4:]) # Slice char 4 to the end of the string
print(str[7:20]) # Notice there is no traceback even though there are not 20 chars

# String concatenation
str = 'Power Rangers'
print(str + ' ' + 'are #1!')
print(str + '!!!')

# Use in as  a logical operator
str = 'Derrick'
print('r' in str)

# String comparison
str = 'Fish Mooney'
if str == 'Fishy': 
    print(True)
else:
    print(False)

if str < 'batman':
    print(True) # Because capital F is less than lowercase b this statement is true
else:
    print(False)

# String methods

# Lowercase
str = 'Derrick M. Strong'
lcstr = str.lower()
print(lcstr)

# Uppercase
ucstr = str.upper()
print(ucstr)
print(dir(str)) # All string methods

# Find
fnd = str.find('r') # Find method
print(fnd) # Prints the position at which 'r' was FIRST found in string

# Advance Find
mailHeader = 'From derrickmacmillions@gmail.com Weds Sept 15 03:17:21 2021'
atPos = mailHeader.find('@')
print(atPos) # 23
spacePos = mailHeader.find(' ', atPos) # Start at the @ sign ie. atPos and keep going until you find a ' ' (space) return position of space
print(spacePos) # 33
host = mailHeader[atPos + 1 : spacePos] # Start right after @ and stop just before ' ' (space)
print(host) # gmail.com

# Replace
rplace = str.replace('M.', 'Malone') # Search and REPLACE first parameter with second parameter
print(rplace)
rplace = str.replace('r', 'p') # Replace all characters not just the first instance
print(rplace)

# Lstrp and Rstrp and Strip
str = '      Hello World  '
lstrp = str.lstrip() # Remove whitespace to the left of the leading (beginning) character
rstrp = str.rstrip() # Remove whitespace to the right of the trailing (ending) character
strp = str.strip() # Strip all whitespace both leading and trailing
print(lstrp)
print(rstrp)
print(strp)

# Startswith
str = 'Happy Gilmore'
startHap = str.startswith('Hap')
startH = str.startswith('h') 
print(startHap) # True string does start with Hap
print(startH) # False string does not start with a lowercase h

# Split
abc = 'Doe ra me'
jack5 = abc.split()
print(jack5)
print(len(jack5))
print(jack5[0])
