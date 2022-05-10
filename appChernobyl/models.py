from django.db import models

# Create your models here.

#Creo clase stalker e importo modelos segun datos a introducir
class Stalkers(models.Model):
    
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    faction = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    dateOfBirth = models.DateField(null=True)

    def __str__(self):
        return self.name+" "+self.surname+" - "+ self.faction     


#Creo clase factions e importo modelos segun datos a introducir
class Factions(models.Model):
    fName = models.CharField(max_length=20, null=True)
    fFounder = models.CharField(max_length=30, null=True)
    fAge = models.IntegerField(null=True)

    def __str__(self):
        return self.fName+" - "+ self.fFounder   

#Creo clase artifacts e importo modelos segun datos a introducir
class Artifacts(models.Model):

    aName = models.CharField(max_length=30, null=True)
    aPower = models.CharField(max_length=30, null=True)
    aDateOfBirth = models.DateField(null=True)

    def __str__(self):
        return self.aName+" - "+ str(self.aPower)


#Creo clase levels e importo modelos segun datos a introducir
class Levels(models.Model):
    lName = models.CharField(max_length=30, null=True)
    lStructureAmount = models.IntegerField(null=True)
    lNpcAmount = models.IntegerField(null=True)
    difficulty = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.lName+" - "+ str(self.lNpcAmount)+" - "+ self.difficulty  

    
