sklad = {
        "1N4148": 250,
        "BAV21": 54,
        "KC147": 147,
        "2N7002": 97,
        "BC547C": 10
    }
key = input("Zadejte kod položky: ")
if key in sklad:
    print("Zadejte množství: ")
else:
    print("Požadované zboží není skladem. ")
number = int
if number in sklad:
    inStock = sklad.pop(number)