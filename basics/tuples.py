# Tuples sorta like List 
# Tuples can't be modified ie. 1) Can't be reassigned 2) Can't sort, append, reverse

x = ('Glenn', 'Sally', 'Molly')
print(x[2])
y = (1, 7, 3)
print(max(y))
print(dir(y)) # count, index

(x, y) = (4, 'fred')
print(y) # fred

d = dict()
d['name'] = 'Derrick'
d['age'] = 42
for (k,v) in d.items():
    print(k,v)

# Comparable
(0, 1, 2) < (5, 1, 2) # True, it checks 0 < 5 which is true and stops comparing
(0, 1, 20000) < (0, 3, 4) # True, it checks 0 < 0 and it can't decide since they are the same so it goes to 1 < 3 which is true and it stops comparing
('Jones', 'Sally') < ('Jones', 'Sam') # True, it checks Jones < Jones and they are equal, checks Sally vs Sam and 'since Sa' are equal it keeps checking but 'l' is less than 'm'

# Sorting Lists of Tuples
d = { 'c': 10, 'b': 7, 'a': 12}
items = d.items()
print(items)
sortedItems = sorted(d.items())
print(sortedItems)

# Loop through and sort a list of Tuples
for (k,v) in sortedItems:
    print(k, v)

# Sort by values instead of key (descending order)
d = {
    'a': 10,
    'b': 7,
    'c': 11
} 
tmp = list() # Create a temporary list to append to later
for (k,v) in d.items():
    tmp.append( (v,k) ) # We append these into a list as values/key pairs

print(tmp)  # [(10, 'a'), (7, 'b'), (11, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp)  # [(11, 'c'), (10, 'a'), (7, 'b')]

# Find top 10 most commmon words in a file
fhand = open('demo.txt') # Create file handle
counts = {} # Create empty dictionary
for line in fhand: # Check each line in demo.txt file
    words = line.split() # Split the words in each line into a list
    for word in words: # Check all the words in words list
        counts[word] = counts.get(word, 0) + 1 # Create histogram to say how frequent a word is found in the file

lst = list() # Create empty list
for (key, val) in counts.items():
    newtuple = (val, key) # Create new tuple
    lst.append(newtuple) # Add newtuples to empty list
lst = sorted(lst, reverse=True) # Sort and reverse tuples

for (val, key) in lst[:10]: # Check the values and keys in the lst (which is a list of tuples) but only the first 10
    print(key, val) # Print out those 10 pairs as key value pairs


# More powerful version of above code
fhand = open('demo.txt')  # Create file handle
counts = {}  # Create empty dictionary
for line in fhand:  # Check each line in demo.txt file
    words = line.split()  # Split the words in each line into a list
    for word in words:  # Check all the words in words list
        # Create histogram to say how frequent a word is found in the file
        counts[word] = counts.get(word, 0) + 1

reversedLst = sorted( [ (v,k) for k,v in counts.items( )], reverse=True ) # Replaces Lines 57-61 in code above called Lamda

# Check the values and keys in the lst (which is a list of tuples) but only the first 10
for (val, key) in reversedLst[:10]:
    print(key, val)  # Print out those 10 pairs as key value pairs
