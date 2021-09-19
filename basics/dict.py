# Dict or Collection like Object

backpack = dict()  # dict constructor
backpack = {}  # shortcut to creating empty dict (same as line above)
backpack['money'] = 100
backpack['book'] = 'Hardknock Life'
backpack['pens'] = 'black fine point'
print(backpack)

# Check if name is in list via Histogram
counts = {}  # create empty dictionary
names = ['Kermit', 'Piggy', 'Happy', 'Dopey',
         'Kermit', 'Happy', 'Piggy', 'Kermit']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)


# Same as Histogram above but using Get method - VERY USEFUL called an Idiom
counts = {}
names = ['Kermit', 'Piggy', 'Frank', 'Happy', 'Dopey',
         'Kermit', 'Happy', 'Piggy', 'Kermit']
for name in names:
    # GET replaces lines 15-19 by saying get the name in name and if it is new set it and give it a value of 0, go back through loop, if its repeated add 1 to its value
    counts[name] = counts.get(name, 0) + 1
print(counts)
