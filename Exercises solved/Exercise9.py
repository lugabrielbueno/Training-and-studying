# Capitalizing a string

# List that will receive some phrases
strings = []

# Receiving a phrases # Calling a method to capitilize
while True:
    strin = str(input('Type a phrase: ')).capitalize()
    if strin:
        strings.append(strin)
    else:
        break

for phrase in strings:
    print(phrase)