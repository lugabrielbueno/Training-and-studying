# Drawing a curve sine vs cousine
#We taking just the positive values for sin, and negative values for cosin

# We'll need the libs: numpy and matplot
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# A function to get only the negative numbers
def negat(x):
    if x > 0:
        x = -x 
    else:
        x = x
    return x

# Creating the lists of values with comprehensions
sin_list = [abs(np.sin(x)) for x in np.linspace(-2*np.pi, 2* np.pi)]
cosin_list = [negat(np.cos(x)) for x in np.linspace(-2*np.pi,2* np.pi)]


# Ploting the lists
with plt.style.context('dark_background'):
    mpl.rcParams['lines.linestyle'] = 'dotted'
    plt.title("A curve of sine(positive) and cosine(negative)")
    plt.plot(list(range(0,50)),sin_list,color = 'red')
    plt.plot(list(range(0,50)),cosin_list,color = 'yellow')
    plt.legend(['Sine','Cosine'])
plt.show()
