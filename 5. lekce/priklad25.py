#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperatu

import pandas
temperature = pandas.read_csv("temperature.csv")
temperature = temperature.set_index("AvgTemperature")

print(temperature.info())
print(temperature.iloc[0:10])
print(temperature[temperature["Day"] == 13])
print(temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")])
print(temperature[(temperature["Day"] == 13) & (temperature["City"] == "Washington")])
print(temperature[(temperature["Day"] == 13) & (temperature["City"] == "Philadelphia")])