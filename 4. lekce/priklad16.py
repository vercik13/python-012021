class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
        return f"Film {self.nazev}, žánr {self.zanr}"

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
        return f"Film {self.nazev}, žánr {self.zanr}, délka filmu {self.delka}"

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def get_info(self):
        return f"Seriál {self.nazev}, žánr {self.zanr}, počet epizod {self.pocet_epizod}, délka epizody {self.delka_epizody}"

film = Film("Pelíšky", "komedie", "120 min")
print(film.get_info())

serial = Serial("How I met your mother", "komedie", "10", "40 min")
print(serial.get_info())