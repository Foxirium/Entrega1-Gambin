from django.http import HttpResponse
from django.shortcuts import render
from appChernobyl.forms import Formulario_Stalkers
from appChernobyl.models import *
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, 'appChernobyl/inicio.html')

def stalkers(request):   

    return render(request, 'appChernobyl/stalkers.html')

def formulario_stalkers(request):


    if request.method == 'POST':

            miFormulario = Formulario_Stalkers(request.POST)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                stalker = Stalkers (name=informacion['name'], surname=informacion['surname'], email=informacion['email'], faction=informacion['faction'], dateOfBirth=informacion['dateOfBirth'])
                stalker.save()
                return render(request, 'appChernobyl/inicio.html') #Vuelvo a inicio

    else:


            miFormulario = Formulario_Stalkers() #Formulario Vacio

    return render(request, 'appChernobyl/formulario_stalkers.html', {"miFormulario":miFormulario})          

def busqueda_stalkers(request):

    return render(request, "appChernobyl/busqueda_stalkers.html")


#Funcion para buscar un stalker
def buscar(request):

    if request.GET["name"]:


        name = request.GET['name']
        stalkers = Stalkers.objects.filter(name__icontains=name)

        return render(request, "appChernobyl/resultado_busquedastalkers.html", {"name":name, "stalkers":stalkers})

    else:

        respuesta = "No se han enviado datos" 



    return HttpResponse(respuesta)              
  


def factions(request):
    return render(request, 'appChernobyl/factions.html')


def artifacts(request):
    return render(request, 'appChernobyl/artifacts.html')


def levels(request):
    return render(request, 'appChernobyl/levels.html')            