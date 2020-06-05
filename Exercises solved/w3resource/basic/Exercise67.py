# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

def conver(n):
    psi = n*0.145038
    bar = n*0.01
    mmhg = n *7.5
    msg = '{} Pounds per square inch\n{} Atmosphere pressure\n{} mmHg'.format(round(psi,4),round(bar,4),round(mmhg,4))
    return msg

print(conver(41))
print(conver(100))