from django.db import models
from material.models import Scanner,Ordinateur,Imprimante,Ecran,Serveur
 


#================DemandeOrdinateur==========================================================


class DemandeOrdinateur(models.Model):
    code_bar = models.AutoField( verbose_name='code bar',primary_key = True,editable=False)
    ordinateur = models.ForeignKey(Ordinateur, on_delete=models.CASCADE ,null=True,to_field='id')
    intervenant = models.CharField( verbose_name='L\'intervenant',max_length=50,null=True)
    fonction_de_intervenant = models.CharField( verbose_name='fonction d\'intervenant',max_length=50,null=True)
    Nature_de_la_panne = models.CharField(max_length=100,null=True)

    les_etats=[
        ('Matériel réparé','Matériel réparé'),
        ('Matériel nécessite intervention externe','Matériel nécessite intervention externe'),
        ('Matériel propose à la réforme','Matériel propose à la réforme')
    ]
    etat_de_demande = models.CharField(max_length=50,choices=les_etats,default='hors service')
    autres = models.CharField(max_length=200,null=True, default='', blank=True)
    def __str__(self):
        return  str(self.code_bar)
#================Demandescanner==========================================================

class DemandeScanner(models.Model):
    code_bar = models.AutoField( verbose_name='code bar',primary_key = True,editable=False)
    Scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE ,null=True, to_field='id')
     
    intervenant = models.CharField( verbose_name='L\'intervenant',max_length=50,null=True)
    fonction_de_intervenant = models.CharField( verbose_name='fonction d\'intervenant',max_length=50,null=True)
    Nature_de_la_panne = models.CharField(max_length=100,null=True)

    les_etats=[
        ('Matériel réparé','Matériel réparé'),
        ('Matériel nécessite intervention externe','Matériel nécessite intervention externe'),
        ('Matériel propose à la réforme','Matériel propose à la réforme')
    ]
    etat_de_demande = models.CharField(max_length=50,choices=les_etats,default='hors service')
    autres = models.CharField(max_length=200,null=True, default='', blank=True)
    def __str__(self):
        return  str(self.code_bar)

#================Demandeimprimante==========================================================

class DemandeImprimante(models.Model):
    code_bar = models.AutoField( verbose_name='code bar',primary_key = True,editable=False)
    Imprimante = models.ForeignKey(Imprimante, on_delete=models.CASCADE ,null=True, to_field='id' )
    
    intervenant = models.CharField( verbose_name='L\'intervenant',max_length=50,null=True)
    fonction_de_intervenant = models.CharField( verbose_name='fonction d\'intervenant',max_length=50,null=True)
    Nature_de_la_panne = models.CharField(max_length=100,null=True)

    les_etats=[
        ('Matériel réparé','Matériel réparé'),
        ('Matériel nécessite intervention externe','Matériel nécessite intervention externe'),
        ('Matériel propose à la réforme','Matériel propose à la réforme')
    ]
    etat_de_demande = models.CharField(max_length=50,choices=les_etats,default='hors service')
    autres = models.CharField(max_length=200,null=True, default='', blank=True)
    def __str__(self):
        return  str(self.code_bar)
#================Demandeecran==========================================================

class DemandeEcran(models.Model):
    code_bar = models.AutoField( verbose_name='code bar',primary_key = True,editable=False)
    Ecran = models.ForeignKey(Ecran, on_delete=models.CASCADE ,null=True, to_field='id')
     
    intervenant = models.CharField( verbose_name='L\'intervenant',max_length=50,null=True)
    fonction_de_intervenant = models.CharField( verbose_name='fonction d\'intervenant',max_length=50,null=True)
    Nature_de_la_panne = models.CharField(max_length=100,null=True)

    les_etats=[
        ('Matériel réparé','Matériel réparé'),
        ('Matériel nécessite intervention externe','Matériel nécessite intervention externe'),
        ('Matériel propose à la réforme','Matériel propose à la réforme')
    ]
    etat_de_demande = models.CharField(max_length=50,choices=les_etats,default='hors service')
    autres = models.CharField(max_length=200,null=True, default='', blank=True)
    def __str__(self):
        return  str(self.code_bar)
#================Demandeserver==========================================================

class DemandeServeur(models.Model):
    code_bar = models.AutoField( verbose_name='code bar',primary_key = True,editable=False)
    Serveur = models.ForeignKey(Serveur, on_delete=models.CASCADE ,null=True, to_field='id')
    
    intervenant = models.CharField( verbose_name='L\'intervenant',max_length=50,null=True,blank=True)
    fonction_de_intervenant = models.CharField( verbose_name='fonction d\'intervenant',max_length=50,null=True)
    Nature_de_la_panne = models.CharField(max_length=100,null=True)

    les_etats=[
        ('Matériel réparé','Matériel réparé'),
        ('Matériel nécessite intervention externe','Matériel nécessite intervention externe'),
        ('Matériel propose à la réforme','Matériel propose à la réforme')
    ]
    etat_de_demande = models.CharField(max_length=50,choices=les_etats,default='hors service')
    autres = models.CharField(max_length=200,null=True, default='', blank=True)
    def __str__(self):
        return  str(self.code_bar)
 