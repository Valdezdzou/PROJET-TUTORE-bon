from django.db import models
from django.contrib.auth.models import AbstractUser

class Fichier(models.Model):
    Titre = models.CharField(max_length=200)
    Auteur = models.CharField(max_length=200)
    nom_du_fichier= models.CharField(max_length=200)
    dernier_contributeur = models.CharField(max_length=200, blank=True)
    date_de_creation = models.DateField()
    date_de_modification = models.DateField(blank=True, null=True)
    sujet = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    document = models.FileField(upload_to='documents', blank=True)
    


    def __str__(self):
         return str(self.nom_du_fichier)
    






