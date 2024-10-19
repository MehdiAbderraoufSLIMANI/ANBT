from django.db import models

class Employe(models.Model):
    
    nom = models.CharField(max_length=30,null=True)
    prenom = models.CharField(max_length=30,null=True)
    Nbureau = models.IntegerField(verbose_name='N°bureau',null=True)
    direction = models.CharField(max_length=50,null=True)
    fonction = models.CharField(max_length=50,null=True)
    addresse_ip = models.CharField(max_length=100,verbose_name='addresse ip',null=True,unique=True)
    def __str__(self):
        return self.prenom+" "+self.nom

