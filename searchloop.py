# Search for value in list
found = False
for val in [9,3,7,4,2,5]:
    if val == 7:
        found = True
        print('Found', val)
        break
if found != True:
    print('Not Found')

# Create a function to find a value in list
def numFound(num, list):
    found = False
    for val in list:
        if val == num:
            found = True
            return  ('Found:', val)
    if found != True:
        return 'Not Found'

randNums = [1,43,65,7,87,9,4,2]
print(numFound(4, randNums))
print(numFound(3, randNums))