#Write a Python program to find the single number in a list that doesn't occur twice

def onlyone(lis):
    for x in lis:
        if lis.count(x) == 1:
            return x

print(onlyone([5, 3, 4, 3, 5, 5, 3]))
print(onlyone([5, 3, 4, 3, 4]))