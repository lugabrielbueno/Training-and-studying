#Write a Python program to convert all units of time into seconds.

def times(y,days,hours,minutes,seconds):
    sec_y = y*365*24*60*60
    sec_day = days*24*60*60
    sec_hours = hours*60*60
    sec_min = minutes*60
    print(sec_y,sec_day,sec_hours,sec_min,seconds)
    return sec_y+sec_day+sec_hours+sec_min+seconds

print(times(4,20,3,42,32))