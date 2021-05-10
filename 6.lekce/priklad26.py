import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzeň = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
zam_praha["město"] = "zam_praha"
zam_plzeň["město"] = "zam_plzeň"
zam_liberec["město"] = "zam_liberec"
zamestnanci = pandas.concat([zam_praha, zam_plzeň, zam_liberec], ignore_index=True)
platy = pandas.read_csv("platy_2021_02.csv")
vysledky_se_jmeny = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"])
print(vysledky_se_jmeny.head())

print(zamestnanci.groupby("město").count())
print(zamestnanci.groupby("město").mean())
