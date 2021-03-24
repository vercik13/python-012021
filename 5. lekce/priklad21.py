#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twlo = pandas.read_csv('twlo.csv')
print(twlo.shape)
print(twlo.iloc[:5])
print(twlo.head())
print(twlo.iloc[-1])
print(twlo.tail())