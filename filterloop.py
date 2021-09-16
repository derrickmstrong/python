# Filter in a Loop
for num in [1,7,20]:
    if num > 5:
        print('Larger than 5:', num)

# Creating function for larger than 5 logic so that it's reuable
def largerThan5(nums):
    for num in nums:
        if num > 5:
            print('Larger than 5:', num)

largerThan5([1,17,34])