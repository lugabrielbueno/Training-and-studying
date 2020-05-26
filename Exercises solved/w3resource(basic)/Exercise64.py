#Write a Python program to get file creation and modification date/times

import os,time

def creat_modf(file):
    pat = os.path.abspath(file)
    (one, two,three,four,five,six,seven , atime,mtime,ctime) = os.stat(pat)
    os.path.getctime
    print('Last modified: %s'%time.ctime(mtime))
    print('Last acess: %s'%time.ctime(atime))
    print('Created: %s'%time.ctime(ctime))

creat_modf('phys.txt')