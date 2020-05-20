import matplotlib.pyplot as plt
import csv
from datetime import datetime

with open('brazilwarming.csv') as fl:
    reader = csv.reader(fl)
    temps, dates = [],[]
    for row in reader:
        try:
            temp = float(row[1])
            date = datetime.strptime(row[0],'%Y-%m-%d')
        except:
            continue
        else:
            temps.append(temp)
            dates.append(date)

fig = plt.figure(None,(10,6))
plt.title('Temperature rise in Brazil from 1830 to 2013',fontsize=20)
plt.ylabel('Temperature(C)',fontsize=15)
plt.plot(dates,temps, c='red',alpha=0.9)
fig.autofmt_xdate()
plt.ylim(21,28)
plt.grid(True)
plt.show()