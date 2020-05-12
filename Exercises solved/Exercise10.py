# Remove the duplicated words and sort the string

# Receiving the string
strin = str(input('Type a phrase: ')).split(' ')

# Counting words, if one of them repeat we remove
for word in strin:
    amount = strin.count(word)
    if amount > 1:
        strin.remove(word)

# Alphabetical order
strin.sort()

# Generating a string with the data
msg = ' '
for word in strin:
    msg = msg+word+' '

print(msg)