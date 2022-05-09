from django import forms


#Formulario para los stalkers
class Formulario_Stalkers(forms.Form):

    name= forms.CharField(max_length=30)
    surname= forms.CharField(max_length=30)
    faction= forms.CharField(max_length=30)
    email= forms.EmailField()
    dateOfBirth= forms.DateField()
    

