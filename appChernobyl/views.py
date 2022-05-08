from django.http import HttpResponse
from django.shortcuts import render
from appChernobyl.models import *
from django.http import HttpResponse


# Create your views here.

def padre(request):
    return render(request, 'appChernobyl/padre.html')

def stalkers(request):
    return render(request, 'appChernobyl/stalkers.html')


def factions(request):
    return render(request, 'appChernobyl/factions.html')


def artifacts(request):
    return render(request, 'appChernobyl/artifacts.html')


def levels(request):
    return render(request, 'appChernobyl/levels.html')            