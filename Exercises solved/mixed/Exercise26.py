#Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.


import numpy as np

def pi_nt(n):
    if n >15:
        return 'So far number'
    else:
        return round(np.pi,n)

print(pi_nt(20))