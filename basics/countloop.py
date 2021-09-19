# Counting in a loop
num = 0
print('Start:', num)
for count in [3,65,86,2,5,667,46,7656,34,36,52,23,334,3,767,68,4]:
    num = num + 1
    print(num, count)
total = num
print('Total:', total)

# Get Sum of numbers in array
sum = 0
print('Start:', sum)
for num in [3,65,86,2,5,667,46,7656,34,36,52,23,334,3,767,68,4]:
    total += num
    print(num, total)
sum = total
print('Sum:', sum)

# Get Average of numbers in array
count = 0
sum = 0
print('Start:', sum)
for num in [3,65,86]:
    count += 1
    sum += num
    print(num, sum, count)
avg = sum/count
print('Avg:', avg)