# Loop through file
# Count to see the most frequent word (bigword) and the number of times it is found in the file (bigcount)
name = input('Enter file name: ') # ask for file name
fhand = open(name) # open provided file name

counts = {} # create empty dictionary
for line in fhand: # iterate through lines in file
    words = line.split() # split each line into list of words
    for word in words: # iterate through each word in the file
        counts[word] = counts.get(word, 0)  + 1 # check to see if word is new or repeated; if new add to dictionary and set val to 0, if repeated add 1 to val to create Histogram
# Find most common value in key/value pair
numoftimesfound = None
mostcommonword = None
for key, val in counts.items(): # loop through each key/val pair of counts dictionary
    if numoftimesfound is None or val > numoftimesfound: # check to see if numoftimesfound is the biggest val we have come across so far or if its still None
        mostcommonword = key
        numoftimesfound = val
print('Most common word in', name + ': ' + mostcommonword)
print('Number of times found in', name + ': ' + str(numoftimesfound))

# Additional Practice
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
