# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years

def interest(amount,interest,years):
    answer = amount*(1+(interest/100))**years
    return round(answer,2)

print(interest(10000,3.5,7))
print(interest(5000,2.5,2))