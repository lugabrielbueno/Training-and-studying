# Write a Python program to get an absolute file path

import os.path as pt

def pathh(file):
    print(pt.abspath(file))

pathh('phys.txt')