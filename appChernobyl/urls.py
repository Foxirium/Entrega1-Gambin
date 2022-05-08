from django.urls import path
from .views import *

urlpatterns = [
    path('', padre, name = 'padre'),
    path('stalkers/', stalkers, name = 'stalkers'),
    path('factions/', factions, name = 'factions'),
    path('artifacts/', artifacts, name = 'artifacts'),
    path('levels/', levels, name = 'levels'),
]