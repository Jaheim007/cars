from pyexpat import model
from django.db import models

class Car(models.Model):     
    nom = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    image= models.FileField()
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
    
    
    def __str__(self):
        return self.nom



# Create your models here.
