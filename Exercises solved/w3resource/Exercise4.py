# Write a Python program which accepts the radius of a circle from the user and compute the

while True:
    try:
        radius = input()
        if not radius:
            break
        radius = float(radius)
    except :
        print("That's not a number, try again.")
    else:
        print(round(3.1415*float(radius)**2,3))
        break