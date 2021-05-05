class Auta:
    def __init__(self, name, registration_plate, km):
        self.name = name
        self.registration_plate = registration_plate
        self.km = km
        self.available = True
    def __str__(self):
        return f"Vozidlo {self.name} registrační značky {self.registration_plate}."


peugeot = Auta("Peugeot 403 Cabrio", "4A2 3020", "47534")

skoda = Auta("Škoda Octavia", "1P3 4747", "41253")

print(peugeot)
print(skoda)