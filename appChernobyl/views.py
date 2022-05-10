from django.http import HttpResponse
from django.shortcuts import render
from appChernobyl.forms import Formulario_Stalkers, Formulario_Factions, Formulario_Artifacts
from appChernobyl.models import *
from django.http import HttpResponse


# Create your views here.
#------------------------------------------------------------------------------------------------------
def inicio(request):
    return render(request, 'appChernobyl/inicio.html')


#------------------------------------------------------------------------------------------------------
#Formulario stalkers
def stalkers(request):


    if request.method == 'POST': #Si entra por Post

            miFormulario = Formulario_Stalkers(request.POST)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                stalker = Stalkers (name=informacion['Name'], surname=informacion['Surname'], email=informacion['Email'], faction=informacion['Faction'], dateOfBirth=informacion['DateOfBirth']) #modelo=informacion[form]
                stalker.save()
                return render(request, 'appChernobyl/inicio.html') #Vuelvo a inicio

    else: #Si entra por Get


            miFormulario = Formulario_Stalkers() #Formulario Vacio

    return render(request, 'appChernobyl/stalkers.html', {"miFormulario":miFormulario})    


#------------------------------------------------------------------------------------------------------
def busqueda_stalkers(request):

    return render(request, "appChernobyl/busqueda_stalkers.html")

#------------------------------------------------------------------------------------------------------
#Funcion para buscar un stalker
def buscar(request):

    if request.GET["name"]:


        name = request.GET['name']
        stalkers = Stalkers.objects.filter(name__icontains=name)

        return render(request, "appChernobyl/resultado_busquedastalkers.html", {"name":name, "stalkers":stalkers}) 

    else:

        respuesta = "No se han enviado datos" 



    return HttpResponse(respuesta)              
  

#------------------------------------------------------------------------------------------------------

#Formulario Facciones
def factions(request):

    if request.method == 'POST': #Si entra por Post

            miFormulario = Formulario_Factions(request.POST)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                factions = Factions (fName=informacion['Name'], fFounder=informacion['Founder'], fAge=informacion['Age']) #modelo=informacion[form]
                factions.save()
                return render(request, 'appChernobyl/inicio.html') #Vuelvo a inicio
    else: #Si entra por Get
        miFormulario = Formulario_Factions() #Formulario Vacio
    return render(request, 'appChernobyl/factions.html', {"miFormulario":miFormulario}) 

   # return render(request, 'appChernobyl/factions.html')

#------------------------------------------------------------------------------------------------------

#Formulario Artefactos
def artifacts(request):

    if request.method == 'POST': #Si entra por Post

            miFormulario = Formulario_Artifacts(request.POST)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                factions = Artifacts (aName=informacion['Name'], aPower=informacion['Power'], aDateOfBirth=informacion['dateOfBirth'])    #modelo=informacion[form]
                factions.save()
                return render(request, 'appChernobyl/inicio.html') #Vuelvo a inicio

    else: #Si entra por Get


            miFormulario = Formulario_Artifacts() #Formulario Vacio

    return render(request, 'appChernobyl/artifacts.html', {"miFormulario":miFormulario}) 

#------------------------------------------------------------------------------------------------------
def levels(request):
    return render(request, 'appChernobyl/levels.html')            