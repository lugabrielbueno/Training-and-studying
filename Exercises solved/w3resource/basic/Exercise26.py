# Write a Python program to create a histogram from a given list of integer

from matplotlib.pyplot import hist,show

def plot_his(lis):
    hist(lis)
    return show()

plot_his([1,2,3,3,4,5,4,1])