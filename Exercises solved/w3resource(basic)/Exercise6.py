 #Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = input('Numbers: ').split(',')
print(numbers)
print(tuple(numbers))