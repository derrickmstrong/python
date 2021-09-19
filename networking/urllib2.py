# urllib

# Create simple web browser (Better/Shorter code than Sockets)

import urllib.request # REQUIRED - Be sure not to name the file as urllib.py

# Open a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

print('\n\n')

# Read a webpage
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
