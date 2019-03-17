from django.db import models

# Create your models here.
from django.db import models


class Variete(models.Model):
    nom = models.CharField(max_length=25)
    desc = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class pot(models.Model):
    potid = models.CharField(max_length=5)
    typepot = models.CharField(max_length=20)
    diampot= models.CharField(max_length=20)
    hautpot= models.CharField(max_length=20)
    fk_Variete = models.ForeignKey(Variete,on_delete=models.CASCADE)

    def __str__(self):
        return self.potid