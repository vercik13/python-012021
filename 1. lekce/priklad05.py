prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
}
key = input("Zadejte název knihy:")
pocet = 0

if key in prodeje2019:
   pocet += prodeje2019[key]

if key in prodeje2020:
   pocet += prodeje2020[key]

print(f'Knihy {key} se prodalo {pocet}');