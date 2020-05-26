#Write a Python program to get the volume of a sphere with a given radius

print('Calculator of sphere volum')
while True:
    try:
        radius = input()
        if not radius:
            break
        radius = float(radius)
    except :
        print("WHOPS! That's not a number, try again")
    else:
        print(round((4/3)*(3.1415)*(radius**3),3))
        break