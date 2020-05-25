#creating a graph and connect all the points in a cartesian plane

import math
import random
import matplotlib.pyplot as plt

x = [random.randint(-100,100) for x in range(0,50)]
y = [random.randint(-100,100) for y in range(0,50)]
z = list(zip(x,y))

plt.scatter(x,y, s =15, color ='red')
plt.grid()
plt.plot([-100,100],[0,0], color = 'black')
plt.plot([0,0],[-100,100], color='black')
plt.plot(x,y,color='blue')
plt.show()