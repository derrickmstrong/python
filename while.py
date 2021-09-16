# Using while keyword

# With break condition
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
    
print('Done!')

# With continue condition
while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)

print('Done!')