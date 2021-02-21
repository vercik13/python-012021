baliky = {"B541X": True, "B547X": False, "B251X": False, "B501X": True, "B947X": False,}
kod = input("Zadejte kód balíku: ")
if kod in baliky:
    baliky = True
    print("Balík byl předán kurýrovi")
else:
    kod in baliky
    baliky = False
    print("Balík zatím nebyl předán kurýrovi")
