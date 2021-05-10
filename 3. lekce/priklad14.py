class Employee:
   def get_info(self):
      return f"{self.name} pracuje na pozici {self.position}."
   def __init__(self, name, position, salary, children):
      self.name = name
      self.position = position
      self.salary = salary
      self.children = children

   def get_net_salary(self):
      dan = self.salary * 0.15 - self.children * 1500
      cista_mzda = self.salary - dan
      return f"Čistá mzda je {cista_mzda}."

#Pokročilejší verze:
   def get_tax(self):
      dan = self.salary * 0.15 - self.children * 1500
      return round(dan)

   def get_net_salary(self):
      net_salary = self.salary - frantisek.get_tax()
      return f"Čistá mzda je {net_salary}."

frantisek = Employee("František Novák", "konstruktér", 30000, 2)

print(frantisek.get_net_salary())