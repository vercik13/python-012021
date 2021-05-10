import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
vykazy = pandas.read_csv("vykazy.csv")

vykazy.to_csv('vykazy.csv', index=False)
#print(vykazy)
print(vykazy.groupby("project")["hours"].sum())