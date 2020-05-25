# Divisible by 5
# Receiving the numbers
numbers = str(input()).split(',')


answer = []

# Looking for the divisors
for number in numbers:
    number = int(number)
    if number % 5 == 0:
        answer.append(str(number))

print(','.join(answer))