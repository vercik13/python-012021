sklad = {
        "1N4148": 250,
        "BAV21": 54,
        "KC147": 147,
        "2N7002": 97,
        "BC547C": 10
    }
key = input("Zadejte kod položky: ")
if key in sklad:
    number = int(input("Zadejte množství: "))
    if sklad [key] >= number:
        print("Poptávku lze uspokojit v plné výši. ")
    if sklad [key] < number:
        print("Lze prodat pouze omezené množství. ")
else:
    print("Požadované zboží není skladem. ")