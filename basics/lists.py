# Lists aka Arrays

print([1, 7, 34])
print(['red', 'blue', 'green'])
print(['name', 'address', ['favorites_foods', 'friends', 'jobs']])

for i in [1, 5, 9, 21]:
    print(i)

# Creates a list with given range ie. 0 up to but not including number provided
print(range(8))
print(len(range(8)))

friends = ['Kermit', 'Ms. Piggy', 'Gonzo', 'Ralph']
print(range(len(friends)))

# loop through friends list (preferred)
for friend in friends:
    print('Happy New Year', friend)

# Same output as above (less preferred)
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)

# Slicing list
print(friends[0:2])
print(friends[1:2])
print(friends[:3])
print(friends[3:])

# All List methods
print(dir(list()))

friends.append('The Lady')  # Append to list (adds to end of list)
print(friends)
friends.reverse()  # Reverses list
print(friends)
print(friends.pop())  # Removes from the end of the list
print(friends)
friends.insert(-1, 'Kermit The Frog')  # Insert before last index (4)
print(friends)
friends.sort()
print(friends)

# list()
newList = list()  # Creates a new blank list
newList.append('book')
newList.append(89)
newList.append('math')
print(newList)

# in/not in operator in list
print(89 in newList)
print('rabbit' in newList)
print('candy' not in newList)

# built-in functions
nums = [3, 5, 7, 2, 58, 31, 49, 2, 4, 59, 7]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


# Compute average using list
numList = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numList.append(value)
    print(numList)

average = sum(numList) / len(numList)
print('Average: ', average)


# Split
abc = 'Doe ra me'
jack5 = abc.split() # Converts the string into a list and with no parameters it looks to split on spaces (also treats a lot of consective spaces as just one space)
print(jack5) # jack5 list
print(len(jack5)) # length of jack5 list
print(jack5[0]) # item at index 0 of jack5 list

for jack in jack5:
    print(jack)

# Double Split
line = 'From: derri@gmail.com Weds Sept 15 08:19:23 2021'
lineParts = line.split() # split the line about by space
email = lineParts[1]
print(email)
emailParts = email.split('@') # split the email apart at '@'
hostname = emailParts[1] # grab the emailPart with index of 1
print(hostname)