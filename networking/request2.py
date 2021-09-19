# Request 

# Create simple web browser (Preferred method)
import requests # REQUIRED - remember to add via sudo pip3 install requests in Terminal

# Open a file
fhand = requests.get('https://www.py4e.com/code/romeo.txt')
print(fhand.text.strip())

# Code below may result in new line in wrong place
# fhand = requests.get('https://www.py4e.com/code/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
