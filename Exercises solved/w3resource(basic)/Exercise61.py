# Write a Python program to convert the distance (in feet) to inches, yards, and miles

def dist(n):
    print(str(round((n*12),4))+' inches')
    print(str(round((n*0.33333),4))+' yards')
    print(str(round((n*0.000189394),4))+' miles')

dist(5)
dist(15)
dist(35)