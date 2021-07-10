from datetime import datetime
#import time
import matplotlib.pyplot as plt

filePath = "C:\\Users\\nicol\\repos\\MyToolbox\\PythonScripts\\CountByDates\\dates.txt"

date_list_full = []
dates_count = {}

with open(filePath) as file:
    for line in file:
        date_string = line.strip()
        date_list_full.append(date_string)

date_list_full.sort(key=lambda date: datetime.strptime(date, '%d/%m/%Y'))

for date in date_list_full:
    if date not in dates_count.keys():
        dates_count[date] = 1
    else:
        dates_count[date] += 1

fontx = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 5}

plt.rc('font', **fontx)

plt.bar(range(len(dates_count)), list(dates_count.values()), align='center')
plt.xticks(range(len(dates_count)), list(dates_count.keys()), rotation='vertical')
plt.yticks(range(0, max(dates_count.values()), 1), fontsize=14)
plt.tight_layout() 
plt.grid()
plt.show()

