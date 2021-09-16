# Regular Expressions
import re  # REQUIRED

# Example 1 - Without RE
hand = open('from.txt')
for line in hand:
    line = line.rstrip()  # Remove trailing whitespace
    if line.find('From:') >= 0:
        print(line)

print('\n')

# Example 1 - With RE
hand = open('from.txt')
for line in hand:
    line = line.rstrip()  # Remove trailing whitespace
    if re.search('From:', line):
        print(line)

print('\n')

# Example 2 - Without RE
hand = open('from.txt')
for line in hand:
    line = line.rstrip()  # Remove trailing whitespace
    if line.startswith('From:'):
        print(line)

print('\n')

# Example 2 - With RE
hand = open('from.txt')
for line in hand:
    line = line.rstrip()  # Remove trailing whitespace
    if re.search('^From:', line):  # ^ - denotes beginning of a line ie. startwith
        print(line)

print('\n')

# Matching and extracting Data
x = 'My 2 favorite numbers are 7 and 11'
y = re.findall('[0-9]+', x)  # extra all numbers
print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)  # extract all email addresses
print(lst)

x = 'From derri.mal@gmail.com Thur Sept 16'
y = re.findall('@([^ ]*)', x)  # extract host out of email address
print(y)

x = 'From derri.mal@gmail.com Thur Sept 16'
# Starting at the beginning of the line where From (plus space) is the start of the line followed by any characters (.*) look for @ then from there extract anything that is not a space and repeat that any number of times IE. extract email address
y = re.findall('^From .*@([^ ]*)', x)
print(y)

# Calculate sum of all transactions using RegEx and Python
x = 'We just received $50.00 pies and $27.90 for cookies' # Initial string value
y = re.findall('\$[0-9.]+', x) # Extract all dollar values
sum = 0 # Create sum placeholder
lst = list() # Create new list
for p in y: # Loop through all dollar values in y
    pattern = r'\$' # Create a pattern to check regex
    x = re.sub(pattern, '', p) # Substitute every thing that matches pattern with blank space
    sum += float(x) # Add all of the values together as you loop through them
    lst.append(sum) # Append values to list 
print('$' + str(lst[-1])) # Print/Concatenate $ plus last item in list - Be sure to convert float to string in order to concatenate

# Calculate sum of all transactions using RegEx and Python
# Initial string value
x = 'We just received $50.00 pies and $27.90 for 30 cookies'
# Extract all dollar values
y = re.findall('\$[0-9.]+', x)
# Create sum placeholder
sum = 0
# Create new list
lst = list()
# Loop through all dollar values in y
for p in y:
    # Create a pattern to check regex
    pattern = r'\$'
    # Substitute every thing that matches pattern with blank space
    x = re.sub(pattern, '', p)
    # Add all of the values together as you loop through them
    sum += float(x)
    # Append values to list
    lst.append(sum)
# Print/Concatenate $ plus last item in list - Be sure to convert float to string in order to concatenate
print('$' + str(lst[-1]))
