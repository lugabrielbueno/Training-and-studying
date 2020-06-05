# Write a Python program to calculate body mass index

def bmi(height,weight):
    return round((weight/height**2),2)

print(bmi(1.7,73))