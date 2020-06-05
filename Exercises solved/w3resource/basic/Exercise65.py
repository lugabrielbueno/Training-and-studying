#Write a Python program to convert seconds to day, hour, minutes and seconds.

from math import floor

def converter(sec):
    days = sec//86400
    hours = (sec/86400)*24 - days*24
    minutes = (hours%1)*60
    seconds = (minutes%1) *60
    return '{} days , {} hours, {} minutes and {} seconds'.format(days,floor(hours),floor(minutes), floor(seconds))

print(converter(80050))