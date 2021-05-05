class Auta:
   def __init__(self, name, registration_mark, km):
      self.name = name
      self.registration_mark = registration_mark
      self.km = km
      self.available = True

   def __str__(self):
      return f"Vozidlo {self.name} registrační značky {self.registration_mark}."

   def pujcAuto(self):
      if self.available == True:
         self.available = False
         return f'Potvrzuji zapůjčení vozidla'
      else:
         return f'Vozidlo není k dispozici'

   def getInfo(self):
      return f'Vozidlo {self.name}, poznávací značky {self.registration_mark}'

   def vratAuto(self, days, stav_tachometru):
      self.stav_tachometru = stav_tachometru
      self.available = True
      cena = 0

      if days <= 7:
         cena += 400 * days
         return f'Cena celkem je {cena} Kč'
      else:
         cena += 300 * days
         return f'Cena celkem za půjčení je {cena} Kč.'

peugeot = Auta('Peugeot 403 Cabrio', '4A2 3020', '47534')
skoda = Auta('Škoda Octavia', '1P3 4747', '41253')

key = input('Jakou značku vozidla si přejete: ')

if key == "peugeot":
   print(peugeot.getInfo())
   print(peugeot.pujcAuto())
else:
   print(skoda.getInfo())
   print(skoda.pujcAuto())

km = int(input('Kolik kilometru jste ujel: '))
days = int(input('Kolik dní bylo auto zapůjčené: '))
print(peugeot.vratAuto(days, km))