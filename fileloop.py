# Loop through file

# Counting pattern to create Histogram
counts = {}
print('Enter a line of text:')
line = input('')
words = line.split()

print('Words: ', words)

print('Counting...')
for word in words:
     counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)

# Loop through dict to get list of keys and values
friends = {
    'chip': 4,
    'dale': 5
}
# Display Key and Value (Hard)
for key in friends:
    print(key, friends[key])

# Other ways of getting a list of keys and values
print(list(friends)) # Returns a list of keys
print(friends.keys()) # Returns a dict_keys list of keys
print(friends.values())  # Returns a dict_values list of values
print(friends.items())  # Returns a dict_items list of keys and values - Tuple pronounces "two tuple"

# Display Two Iteration Variables ie. Key and Value (Easy)
for key, val in friends.items():
    print(key, val)
