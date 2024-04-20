def alphabet_generator():
    current = ord('A')
    while current <= ord('Z'):
        yield chr(current)
        current += 1

# create an instance of iterator
alpha_ite = alphabet_generator()

# iterate over aplhabet and print
for letter in alpha_ite:
    print(letter, end=' ')
print('')





def interval_generator():
    current = 1
    while current <= 10:
        yield current
        current += 0.5

# Create an instance of the generator
interval_iter = interval_generator()

# Iterate over the intervals and print them
for interval in interval_iter:
    print(interval, end=' ')
print('')
