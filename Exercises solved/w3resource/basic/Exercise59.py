#Write a Python program to convert height (in feet and inches) to centimeters


def meter_to_feet(n):
    return round((n*3.28084),2)

def inch_to_cm(n):
    return round((n/0.393701),2)

print(meter_to_feet(10))
print(inch_to_cm(24))