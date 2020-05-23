#Comparison between Sitka and the Death Valley: Temperature scales in the Sitka and Death Valley charts reflect the different data ranges. To compare the temperature variations between Sitka and the Death Valley so precise, it is necessary to use identical scales on the y axis. Change the settings of the y-axis on one of the graphs in Figures 16.5 and 16.6, or both, and make a direct comparison between temperature variations in Sitka and in the Death Valley (or any two places you want to compare). You can also try to plot the two data sets on the same graph.

from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Opening the files .csv
with open('death_valley_2018_simple.csv') as fl:
    #we'll read each line making a list, like an array
    reader = csv.reader(fl)

    #Creating the lists that will be plotted
    dates, maxis, minins = [],[],[]
    for row in reader:
        try:
            #creating the errors corrections in case of empty cells or invalid content
            mx = int(row[4])
            mn = int(row[5])
            date = datetime.strptime(row[2],'%Y-%m-%d')
        except :
            #jumping the error
            continue
        else:
            #appendind each value on the list
            dates.append(date)
            maxis.append(mx)
            minins.append(mn)
    
    #repeat all the process here
    with open('sitka_weather_2018_simple.csv') as file:
        readeer = csv.reader(file)

        minns,maxx,datess = [],[],[]
        for row in readeer:
            try:
                mxx = int(row[5])
                minn = int(row[6])
                date = datetime.strptime(row[2],'%Y-%m-%d')
            except:
                continue
            else:
                maxx.append(mxx)
                minns.append(minn)
                datess.append(date)

fig = plt.figure(None,(10,6))
plt.title('Comparing temperatures between Death Valley in CA and Sitka in AK')
plt.ylabel('Temperature(F)')
plt.plot(dates,maxis,c='red')
plt.plot(dates,minins, c='blue')
plt.fill_between(dates,maxis,minins,color='red',alpha = 0.8)
plt.plot(datess,maxx,c='green')
plt.plot(datess,minns,c='yellow')
plt.fill_between(datess,maxx,minns,color='green',alpha = 0.8)
fig.autofmt_xdate()
plt.legend(['Max(DV)','Min(DV)','Max(Sk)','Min(Sk)'])
plt.show()