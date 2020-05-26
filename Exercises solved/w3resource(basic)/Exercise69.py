# Write a Python program to sort three integers without using conditional statements and loops.

def sortint(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    return lista

print(sortint(4,8,1))