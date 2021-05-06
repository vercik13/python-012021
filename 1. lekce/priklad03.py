volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
number = int(input("Zadejte číslo hodiny: "))
if number in volnePokoje:
    free = volnePokoje.pop(number)
    print(f"K dispozici je: {free}. ")
else:
    print("Bohužel žádný pokoj není volný. ")
