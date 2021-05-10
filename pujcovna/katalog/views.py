from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from . import models
from django.urls import reverse_lazy

class IndexView(View):
    def get(self, request):
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
        <a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>
        <h2>O naší autopůjčovně</h2>
        <p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
        <h2>Využijte dlouhodobý pronájem vozu!</h2>
        <p>Auto Vám můžeme dovézt až domů!</p>
        <a>Dlouhodobý pronájem aut.</a><br>
        <p>Naše programy a služby.</p>
        """)

class SeznamView(ListView):
    #def get(self, request):
    #    return HttpResponse("Zde bude seznam aut.")
    model = models.Auto
    template_name = "katalog/seznam_list.html"

class PrehledVypujcek(ListView):
    model = models.Vypujcka
    template_name = "katalog/vypujcky_list.html"

class PrehledZakaznik(ListView):
    model = models.Zakaznik
    template_name = "katalog/zakaznik_list.html"

class PrehledAuto(ListView):
    model = models.Auto
    template_name = "katalog/auto_list.html"

class DetailVypujckyView(DetailView):
    model = models.Vypujcka
    template_name = "katalog/vypujcky_detail.html"

class DetailZakaznikView(DetailView):
    model = models.Zakaznik
    template_name = "katalog/zakaznik_detail.html"

class DetailAutoView(DetailView):
    model = models.Auto
    template_name = "katalog/auto_detail.html"

class PridejAutomobil(CreateView):
    model = models.PridaniAutomobilu
    template_name = "pridani automobilu/pridaniautomobilu.html"
    fields = ["registracni_znacka", "znacka_vozidla", "pocet_kilometru", "datum_tech_kontroly"]
    success_url = reverse_lazy("potvrzeni.html")

class PotvrzeniPridani(TemplateView):
    template_name = "pridani automobilu/potvrzeni.html"

class PridejVypujcku(CreateView):
    model = models.PridaniVypujcky
    template_name = "pridani vypujcky/pridanivypujcky.html"
    fields = ["datum_cas_vypujcky", "datum_cas_konce_vypujcky", "cena_vypujcky", "zakaznik", "auto"]
    success_url = reverse_lazy("potvrzenivypujcky.html")

class PotvrzeniPridaniVypujcky(TemplateView):
    template_name = "pridani vypujcky/potvrzenivypujcky.html"
