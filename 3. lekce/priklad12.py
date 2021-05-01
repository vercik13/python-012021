class Auta:
    def __init__(self, name, registration_plate, km):
        self.name = name
        self.registration_plate = registration_plate
        self.km = km
        self.available = True

    def pujc_auto(self):
        self.available = False

    def get_info(self):
        if self.available:
            return f"Potvrzuji zapůjčení vozidla {self.name}, registrační značky {self.registration_plate}."
        return f"Vozidlo {self.name} není k dispozici"

peugeot = Auta("Peugeot 403 Cabrio", "4A2 3020", 47534 )
skoda = Auta("Škoda Octavia", "1P3 4747", 41253 )

input("Jaké vozidlo si přejete půjčit: ")
print(peugeot.get_info())
peugeot.pujc_auto()
print(peugeot.get_info())

input("Jaké vozidlo si přejete půjčit: ")
print(skoda.get_info())
skoda.pujc_auto()
print(skoda.get_info())