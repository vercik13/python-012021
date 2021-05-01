#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv("temperature.csv")
temperature = temperature.set_index("City")

print(temperature.iloc[0:10])
print(temperature.info)
print(temperature.loc[["Prague"]])
print(temperature[temperature["AvgTemperature"] > 80])
print(temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")])
print(temperature[temperature["AvgTemperature"] > 80])
print(temperature[temperature["AvgTemperature"] < -20])