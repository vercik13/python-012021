from django.urls import path
from . import views

urlpatterns = [
path('', views.IndexView.as_view(), name='katalog'),
path('seznam/', views.SeznamView.as_view(), name='seznam'),
path('vypujcky/', views.PrehledVypujcek.as_view(), name='vypujcky'),
path('zakaznici/', views.PrehledZakaznik.as_view(), name='zakaznici'),
path('auto/', views.PrehledAuto.as_view(), name='auto'),
path('vypujcka/<int:pk>', views.DetailVypujckyView.as_view(), name='detail_vypujcka'),
path('zakaznici/<int:pk>', views.DetailZakaznikView.as_view(), name='detail_zakaznik'),
path('auto/<int:pk>', views.DetailAutoView.as_view(), name='detail_auto'),
path("pridaniautomobilu/", views.PridejAutomobil.as_view(), name="pridaniautomobilu.html"),
path("pridaniautomobilu/potvrzeni/", views.PotvrzeniPridani.as_view(), name="potvrzeni.html"),
path("pridanivypujcky/", views.PridejVypujcku.as_view(), name="pridanivypujcky.html"),
path("pridanivypujcky/potvrzenivypujcky/", views.PotvrzeniPridaniVypujcky.as_view(), name="potvrzenivypujcky.html"),
]
