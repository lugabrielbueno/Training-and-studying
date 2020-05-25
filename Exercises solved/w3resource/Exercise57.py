#Write a program to get execution time for a Python method

import time

start = time.time()
'Hello, world'.split()
final = time.time()
total_time = final - start
print(str(total_time*1000)+' ms')