#with open("weather_data.csv") as file:
#    wd = file.readlines()
#
#print(wd)
#

#import csv
#
#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#
#print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

#data_dict = data.to_dict()
#
#temp_list = data["temp"].to_list()
#print(temp_list)
#
#ave = sum(temp_list)/len(temp_list)
#print(ave)
#
#print(data["temp"].mean())
#print(data["temp"].max())

#row = data[data.day == "Monday"]
#print(row.temp[0])

#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp[0])