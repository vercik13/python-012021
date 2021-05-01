#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

import pandas
country_vaccinations = pandas.read_csv("country_vaccinations.csv")

pocty_ockovanych = country_vaccinations[(country_vaccinations["date"] == "2021-03-10") & (country_vaccinations["total_vaccinations"])]
print(pocty_ockovanych["total_vaccinations"])

pocty_lidi = country_vaccinations[(country_vaccinations["daily_vaccinations"] > 1_000_000) & (country_vaccinations["date"] == "2021-03-10")]
print(pocty_lidi)
vice_lidi = country_vaccinations[(country_vaccinations["daily_vaccinations"] > 100_000) & (country_vaccinations["date"] == "2021-03-10")]
print(vice_lidi)
mene_lidi = country_vaccinations[(country_vaccinations["daily_vaccinations"] < 100_000) & (country_vaccinations["date"] == "2021-03-10")]
print(mene_lidi)
print(country_vaccinations[country_vaccinations["country"].isin(["United Kingdom", "Finland", "Italy"]) & (country_vaccinations["date"] == "2021-03-10")])
print(country_vaccinations[country_vaccinations["country"].isin(["United Kingdom", "Finland", "Italy"]) & (country_vaccinations["date"] == "2021-03-11")])