# Working with files

fhand = open('demo.txt', 'r') # Returns a handle to open file in read mode (other modes are write)
print(fhand) # The handle is a wrapper that lets you get to the data in the file but isn't data itself

# Loop through and print each line of the file myfile
myfile = open('demo.txt')
for line in myfile:
    print(line + '\n')

# Count the number of lines in the file (lines are determined by the number of \n chars in file)
myfile = open('demo.txt')
count = 0
for line in myfile:
    count += 1
print('Number of lines:', count)

# Count number of characters in a file
fhand = open('demo.txt') # Returns handle
myfile = fhand.read() # Reads fileand put it in one big blob
print('Number of characters:', len(myfile)) # Returns length in characters
print('First 5 chars:', myfile[:5]) # Returns characters up to but not including index 5

# Search through file to find how many times 'minx' appears in file
fhand = open('demo.txt')
count = 0
for line in fhand:
    if 'minx' in line:
        count += 1
print('Found "minx" ' + str(count) + ' times in file')

# Create function to search through file for lines that startswith specific text
def linePrefix(txt, file):
    fhand = open(file)
    count = 0
    for line in fhand:
        if line.startswith(txt):
            count +=1
    return 'Found ' + str(count) + ' lines that start with ' + txt

print(linePrefix('Duis', 'demo.txt'))
print(linePrefix('Lorem', 'demo.txt'))
print(linePrefix('Lo', 'demo.txt'))

# Search through file to file selected phrases
fhand = open('from.txt')
for line in fhand:
    line = line.rstrip() # VERY COMMON pattern - Remove/Strip right newline char
    if line.startswith('From:'):
        print(line)

# Same logic as above
fhand = open('from.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# Collect filename as input (in order to evaluate different files) and count how many times minx is found in specified file
fname = input('Enter a filename: ')
# Added try/except for cases where user enter in invalid file name
try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    quit() # Must add quit() to terminal program silently

count = 0
for line in fhand:
    if 'minx' in line:
        count += 1
print('minx found ' + str(count) + ' times in ' + fname + '.')

# Similiar to above but creating function searching for specific prefix in file and only printing those lines
def findPrefixInFile(prefix, file):
    fhand = open(file)
    for line in fhand:
        if line.startswith(prefix):
             print(line.rstrip())

print(findPrefixInFile('To', 'from.txt'))
print(findPrefixInFile('From', 'from.txt'))