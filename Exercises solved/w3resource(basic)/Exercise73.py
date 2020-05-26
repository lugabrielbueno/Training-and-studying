#Write a Python program to calculate midpoints of a line

def mid(x1,y1,x2,y2):
    xm = (x1+x2)/2
    ym = (y1+y2)/2
    return xm,ym

print(mid(2,4,5,9))
print(mid(0,0,8,1))