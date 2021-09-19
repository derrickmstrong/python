# Find smallest num in loop using None and is
smallest = None
for num in [2,5,8,1,89,34,11,6,7]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print('Smallest num:', smallest)