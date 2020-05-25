# Divisible by 7 but not by 5

# List that have all the divisors
list_divisors = []

# Verify all the numbers in the interval
for number in range(2000,3201):
    
    # If divisible by 7 and dont divisible by 5 OK!
    if number % 7 == 0 and number % 5 != 0 :
        list_divisors.append(number)
print(list_divisors)