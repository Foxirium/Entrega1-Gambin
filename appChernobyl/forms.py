from django import forms

#-------------------------------------------------------------------------
#Clase Formulario Stalkers
class Formulario_Stalkers(forms.Form):

    Name= forms.CharField(max_length=30)
    Surname= forms.CharField(max_length=30)
    Faction= forms.CharField(max_length=30)
    Email= forms.EmailField()
    DateOfBirth= forms.DateField()

#-------------------------------------------------------------------------
#Clase Formulario Facciones
class Formulario_Factions(forms.Form):

    Name = forms.CharField(max_length=20) 
    Founder = forms.CharField(max_length=30)
    Age = forms.IntegerField()

#-------------------------------------------------------------------------
#Clase Formulario Artefactos
class Formulario_Artifacts(forms.Form):

    Name = forms.CharField(max_length=30)
    Power = forms.CharField(max_length=30)
    dateOfBirth= forms.DateField()

    

