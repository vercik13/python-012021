from django.db import models

class Auto(models.Model):
    registracni_znacka = models.CharField(max_length=100)
    znacka_vozidla = models.CharField(max_length=100)
    pocet_kilometru = models.IntegerField()
    datum_tech_kontroly = models.DateField()

    def __str__(self):
        return self.znacka_vozidla

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=1000)
    cislo_ridicskeho_prukazu = models.CharField(max_length=100)
    def __str__(self):
        return self.prijmeni

class Vypujcka(models.Model):
    datum_cas_vypujcky = models.DateTimeField()
    datum_cas_konce_vypujcky = models.DateTimeField()
    cena_vypujcky = models.IntegerField()
    zakaznik = models.ForeignKey("Zakaznik", on_delete=models.SET_NULL, null=True)
    auto = models.ForeignKey("Auto", on_delete=models.SET_NULL, null=True)


class PridaniAutomobilu(models.Model):
    registracni_znacka = models.CharField(max_length=100)
    znacka_vozidla = models.CharField(max_length=100)
    pocet_kilometru = models.IntegerField()
    datum_tech_kontroly = models.DateField()

    def __str__(self):
        return self.znacka_vozidla

class PridaniVypujcky(models.Model):
    datum_cas_vypujcky = models.DateTimeField()
    datum_cas_konce_vypujcky = models.DateTimeField()
    cena_vypujcky = models.IntegerField()
    zakaznik = models.ForeignKey("Zakaznik", on_delete=models.SET_NULL, null=True)
    auto = models.ForeignKey("Auto", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.auto