from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('stalkers/', stalkers, name = 'stalkers'),
    path('factions/', factions, name = 'factions'),
    path('artifacts/', artifacts, name = 'artifacts'),
    path('levels/', levels, name = 'levels'),
    path('formulario_stalkers/', formulario_stalkers, name= 'formulario_stalkers'),
    path('busqueda_stalkers/', busqueda_stalkers, name = 'busqueda_stalkers'),
    path('buscar/', buscar),
    path('resultado_busqueda/', buscar),

]