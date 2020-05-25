#Convert a number to word

import inflect

number = int(input('Number: '))
n = inflect.engine()
print(n.number_to_words(number).title())