from ast import mod
from django.db import models
from django.utils.html import format_html
from employes.models import Employe
les_etat=[
('Hors service','Hors service'),
('Fonctionne','Fonctionne'),
('Traitement','Traitement')
]
#================ordinateur==========================================================
class Ordinateur(models.Model):
    numero_inventaire = models.CharField(max_length=100,verbose_name='numero d\'inventaire',unique = True)
    numero_serie = models.CharField(verbose_name='numero serie',max_length=100,null=True,unique = True)
    Employe_que_gerer = models.ForeignKey(Employe, on_delete=models.PROTECT,null=True)
    marque = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    taille_de_disque_dur = models.CharField(max_length=100,verbose_name='taille de disque dur')
    ram = models.CharField(max_length=100)
    
    system_d_exploitation = models.CharField(max_length=100,verbose_name='system d\'exploitation')
    etat_de_materiel = models.CharField(max_length=100,verbose_name='etat de materiel',choices=les_etat,default='Fonctionne')
    def __str__(self):
        return self.numero_inventaire
    def etat_de_materiel_(self):
        if self.etat_de_materiel == "Hors service":
            return format_html('<span style="color: rgb(221, 0, 0);font-weight: bold;">{0}</span> ',self.etat_de_materiel)
        elif self.etat_de_materiel == "Fonctionne":
            return format_html('<span style="color: rgb(0, 172, 0);font-weight: bold;">{0}</span>',self.etat_de_materiel)
        elif self.etat_de_materiel == "Traitement":
            return format_html('<span style="color: rgb(235, 91, 8);font-weight: bold;">{0}</span>',self.etat_de_materiel)
    scanner = models.OneToOneField("Scanner",blank=True,on_delete=models.PROTECT,null=True)
    imprimante = models.OneToOneField("Imprimante",blank=True,on_delete=models.PROTECT,null=True)
    ecran = models.OneToOneField("Ecran",blank=True,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.numero_inventaire

#=====================Scanner=====================================================
class Scanner(models.Model):
    
    numero_inventaire = models.CharField(max_length=100,verbose_name='numero d\'inventaire',unique = True)
    numero_serie = models.CharField(verbose_name='numero serie',max_length=100,null=True,unique = True)
    marque = models.CharField(max_length=100,null=True)
    resolution = models.CharField(max_length=100,null=True)
    dimension = models.CharField(max_length=100,null=True)
    etat_de_materiel = models.CharField(max_length=100,verbose_name='etat de materiel',choices=les_etat,default='Fonctionne')
    def __str__(self):
        return self.numero_inventaire
    def etat_de_materiel_(self):
        if self.etat_de_materiel == "Hors service":
            return format_html('<span style="color: rgb(221, 0, 0);font-weight: bold;">{0}</span> ',self.etat_de_materiel)
        elif self.etat_de_materiel == "Fonctionne":
            return format_html('<span style="color: rgb(0, 172, 0);font-weight: bold;">{0}</span>',self.etat_de_materiel)
        elif self.etat_de_materiel == "Traitement":
            return format_html('<span style="color: rgb(235, 91, 8);font-weight: bold;">{0}</span>',self.etat_de_materiel)



#=====================Imprimante=====================================================

class Imprimante(models.Model):
    numero_inventaire = models.CharField(max_length=100,verbose_name='numero d\'inventaire',unique = True)
    numero_serie = models.CharField(verbose_name='numero serie',max_length=100,null=True,unique = True)
    marque = models.CharField(max_length=100)
    etat_de_materiel = models.CharField(max_length=100,verbose_name='etat de materiel',choices=les_etat,default='Fonctionne')
    type = models.CharField(max_length=100,verbose_name='type')
    resolution = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    def __str__(self):
        return self.numero_inventaire
    def etat_de_materiel_(self):
        if self.etat_de_materiel == "Hors service":
            return format_html('<span style="color: rgb(221, 0, 0);font-weight: bold;">{0}</span> ',self.etat_de_materiel)
        elif self.etat_de_materiel == "Fonctionne":
            return format_html('<span style="color: rgb(0, 172, 0);font-weight: bold;">{0}</span>',self.etat_de_materiel)
        elif self.etat_de_materiel == "Traitement":
            return format_html('<span style="color: rgb(235, 91, 8);font-weight: bold;">{0}</span>',self.etat_de_materiel)

#=====================Ecran=====================================================

class Ecran(models.Model):
    numero_inventaire = models.CharField(max_length=100,verbose_name='numero d\'inventaire',unique = True)
    numero_serie = models.CharField(verbose_name='numero serie',max_length=100,null=True,unique = True)
    marque = models.CharField(max_length=100)
    taille_de_lecran = models.CharField(max_length=100,verbose_name='taille de l\'ecran')
    etat_de_materiel = models.CharField(max_length=100,verbose_name='etat de materiel',choices=les_etat,default='Fonctionne')
    def __str__(self):
        return self.numero_inventaire
    def etat_de_materiel_(self):
        if self.etat_de_materiel == "Hors service":
            return format_html('<span style="color: rgb(221, 0, 0);font-weight: bold;">{0}</span> ',self.etat_de_materiel)
        elif self.etat_de_materiel == "Fonctionne":
            return format_html('<span style="color: rgb(0, 172, 0);font-weight: bold;">{0}</span>',self.etat_de_materiel)
        elif self.etat_de_materiel == "Traitement":
            return format_html('<span style="color: rgb(235, 91, 8);font-weight: bold;">{0}</span>',self.etat_de_materiel)

#=====================SErver=====================================================

class Serveur(models.Model):
    numero_inventaire = models.CharField(max_length=100,verbose_name='numero d\'inventaire',unique = True)
    numero_serie = models.CharField(verbose_name='numero serie',max_length=100,null=True,unique = True)
    nom_du_serveur = models.CharField(max_length=100,verbose_name='nom du serveur')
    Employe_que_gerer = models.ForeignKey(Employe, on_delete=models.PROTECT,null=True)
    processeur = models.CharField(max_length=100)
    taille_de_disque_dur = models.CharField(max_length=100,verbose_name='taille de disque dur')
    ram = models.CharField(max_length=100)
    system_d_exploitation = models.CharField(max_length=100,verbose_name='system d\'exploitation')
    etat_de_materiel = models.CharField(max_length=100,verbose_name='etat de materiel',choices=les_etat,default='Fonctionne')
    class Meta:
        verbose_name = 'Serveur'
    def __str__(self):
        return self.numero_inventaire
    def etat_de_materiel_(self):
        if self.etat_de_materiel == "Hors service":
            return format_html('<span style="color: rgb(221, 0, 0);font-weight: bold;">{0}</span> ',self.etat_de_materiel)
        elif self.etat_de_materiel == "Fonctionne":
            return format_html('<span style="color: rgb(0, 172, 0);font-weight: bold;">{0}</span>',self.etat_de_materiel)
        elif self.etat_de_materiel == "Traitement":
            return format_html('<span style="color: rgb(235, 91, 8);font-weight: bold;">{0}</span>',self.etat_de_materiel)

