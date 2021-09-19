# Find the largest number in array
largest_so_far = -1
for num in [2,45,65,3,70,32]:
    if num > largest_so_far: # Check if num is larger than previous largest_number_so_far
        largest_so_far = num
        print(largest_so_far)

largest = largest_so_far
print('Largest Number:', largest)