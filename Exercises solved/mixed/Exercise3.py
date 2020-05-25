# Squared dictionary

# Receiving the number
n = int(input('Type a number: '))

# Squared dict
squared = {}

# Calculating and add on dict
for number in range(1,n+1):
    x = number**2

    # Adding on dict the key value pairs
    squared[number] = x

print(dict(squared))