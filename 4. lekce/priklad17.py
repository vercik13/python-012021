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
   def get_celkova_delka(self):
      return self.delka

class Serial(Polozka):
   def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
      super().__init__(nazev, zanr)
      self.pocet_epizod = pocet_epizod
      self.delka_epizody = delka_epizody
      self.celkova_delka = pocet_epizod * self.delka_epizody
   def get_celkova_delka(self):
      return self.celkova_delka
   def get_info(self):
      return f"Seriál {self.nazev}, žánr {self.zanr}, počet epizod {self.pocet_epizod}, délka epizody {self.delka_epizody}"

class Uzivatel(Polozka):
   def __init__(self, uzivatelske_jmeno):
      self.uzivatelske_jmeno = uzivatelske_jmeno
      self.zhlednute = []
   def pripocti_zhlednuti(self, polozka):
      self.zhlednute.append(polozka)
   def delka_sledovani(self):
      delka = 0
      for polozka in self.zhlednute:
         delka += polozka.get_celkova_delka()
      return delka


film = Film("Pelíšky", "komedie", 120)
print(film.get_info())

serial = Serial("How I met your mother", "komedie", 10, 40)
print(serial.get_info())

veronika = Uzivatel("Veronika")
veronika.pripocti_zhlednuti(film)
veronika.pripocti_zhlednuti(serial)
print(f'Uživatel {veronika.uzivatelske_jmeno} sledoval {veronika.delka_sledovani()} minut.')