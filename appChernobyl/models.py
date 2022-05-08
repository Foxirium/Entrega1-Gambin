from django.db import models
from django.forms import CharField, DateField, EmailField, IntegerField

# Create your models here.

#Creo clase stalker e importo modelos segun datos a introducir
class Stalkers(models.Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    faction = CharField(max_length=30)
    email = EmailField()
    dateOfBirth = DateField()

#Creo clase factions e importo modelos segun datos a introducir
class Factions(models.Model):
    fName = CharField(max_length=20)
    fLeader = CharField(max_length=30)
    fage = IntegerField()

#Creo clase artifacts e importo modelos segun datos a introducir
class Artifacts(models.Model):
    aName = CharField(max_length=30)
    aPower = CharField(max_length=30)
    aDateOfBirth = DateField()

#Creo clase levels e importo modelos segun datos a introducir
class Levels(models.Model):
    lName = CharField(max_length=30)
    lstrucamount = IntegerField()

    
