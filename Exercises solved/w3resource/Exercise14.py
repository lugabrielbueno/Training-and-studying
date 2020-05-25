#Write a Python program to calculate number of days between two dates.

print('Type the dates with comma-separated (format: YYYY,MM,DD)')

while True:
    try:
        date1 = input('Initial date: ').split(',')
        
        date2 = input('Final date: ').split(',')
        if not date1 or not date2:
            break
        initialday = int(date1[-1])
        finalday = int(date2[-1])
    except :
        print('Format invalid, try again.')
    else:
        days = finalday - initialday
        print(str(days)+ ' days')
        break