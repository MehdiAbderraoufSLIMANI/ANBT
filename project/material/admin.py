from calendar import c
from django.contrib import admin
from .models import Ordinateur,Scanner,Imprimante,Ecran,Serveur
from Demandes.models import DemandeOrdinateur,DemandeScanner,DemandeEcran,DemandeImprimante,DemandeServeur
from django.contrib.auth import get_user_model
from datetime import datetime
from ctypes import alignment
from django.http import HttpResponse
import xlwt

 
class OrdinateurInline(admin.StackedInline):
    model =Ordinateur 
    fields = ('Employe_que_gerer','numero_inventaire','numero_serie',)
    readonly_fields = fields
    extra = 0
    can_delete = False
    show_change_link = True
    max_num=0

    def has_add_permission(self, request, obj=None):
        return False
#===================Scanner=================================

class CustomAdmin(admin.ModelAdmin):
    readonly_fields= ('ordinateur',)

class DemandeScannerInline(admin.StackedInline):
    model =DemandeScanner 
    extra = 0
    show_change_link = True
    readonly_fields= ('intervenant','fonction_de_intervenant')


class CustomScannerDemandeAdmin(admin.ModelAdmin):
    inlines = [
        DemandeScannerInline,
        OrdinateurInline,
    ]
    search_fields = ['numero_inventaire'] 
    list_filter =  ['etat_de_materiel']
    list_display = ['numero_inventaire','numero_serie','etat_de_materiel_','marque','resolution','dimension']

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Scanner' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Scanner')
        row_num = 1
        columns = [field.verbose_name for field in meta.fields]
        font_style = xlwt.XFStyle()
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.HAIR
        borders.right = xlwt.Borders.HAIR
        borders.top = xlwt.Borders.HAIR
        borders.bottom = xlwt.Borders.HAIR
        font_style.borders = borders
        
        font_styleA = font_style
        font_style.font.bold = True

        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(columns[col_num]), font_style)

        row = []

        for obj in queryset:
            for field in fieldnames:
                if getattr(obj,field) == None:
                    a = ''
                else:
                    a = getattr(obj,field)
                    
                row.append(a)
                if len(row)== len(fieldnames):
                    
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_styleA)
                    row = []
        wb.save(response)
        return response
    export_to_csv.short_description = "Export"    
admin.site.register(Scanner,CustomScannerDemandeAdmin)


#===================ordinateur================================

class DemandeOrdinateurInline(admin.StackedInline):
    model =DemandeOrdinateur 
    extra = 0
    show_change_link = True
    readonly_fields= ('intervenant','fonction_de_intervenant')


class CustomordinateurDemandeAdmin(admin.ModelAdmin):

    inlines= [DemandeOrdinateurInline,]
    search_fields = ['numero_inventaire'] 
    list_filter =  ['etat_de_materiel']
    list_display = ['numero_inventaire','numero_serie','etat_de_materiel_','marque','Employe_que_gerer','processeur','taille_de_disque_dur','ram','system_d_exploitation']
    raw_id_fields=['Employe_que_gerer','scanner','imprimante','ecran',]

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=ordinateur' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Ordinateur')
        row_num = 1
        columns = [field.verbose_name for field in meta.fields]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.HAIR
        borders.right = xlwt.Borders.HAIR
        borders.top = xlwt.Borders.HAIR
        borders.bottom = xlwt.Borders.HAIR
        font_style.borders = borders
        font_style.alignment.wrap = 1
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(columns[col_num]), font_style)
            
        row = []

        for obj in queryset:
            for field in fieldnames:
                if getattr(obj,field) == None:
                    a = ''
                else:
                    a = getattr(obj,field)
                row.append(a)
                if len(row)== len(fieldnames):
                    
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                    row = []
        wb.save(response)
        return response
    export_to_csv.short_description = "Export"    
admin.site.register(Ordinateur,CustomordinateurDemandeAdmin)

#===================Imprimante=================================
class DemandeImprimanteInline(admin.StackedInline):
    model =DemandeImprimante 
    extra = 0
    show_change_link = True

    readonly_fields= ('intervenant','fonction_de_intervenant')


class CustomDemandeimprimanteAdmin(admin.ModelAdmin):

    inlines= [DemandeImprimanteInline,OrdinateurInline,]
    search_fields = ['numero_inventaire'] 
    list_filter =  ['etat_de_materiel']
    list_display = ['numero_inventaire','numero_serie','etat_de_materiel_','marque','resolution','dimension','type']

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=imprimante' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('imprimante')
        row_num = 1
        columns = [field.verbose_name for field in meta.fields]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.HAIR
        borders.right = xlwt.Borders.HAIR
        borders.top = xlwt.Borders.HAIR
        borders.bottom = xlwt.Borders.HAIR
        font_style.borders = borders
        font_style.alignment.wrap = 1
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(columns[col_num]), font_style)

        row = []

        for obj in queryset:
            for field in fieldnames:
                if getattr(obj,field) == None:
                    a = ''
                else:
                    a = getattr(obj,field)
                row.append(a)
                if len(row)== len(fieldnames):
                    
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                    row = []
        wb.save(response)
        return response
    export_to_csv.short_description = "Export"    
admin.site.register(Imprimante,CustomDemandeimprimanteAdmin)

#===================Ecran=================================
class DemandeEcranInline(admin.StackedInline):
    model =DemandeEcran 
    extra = 0
    show_change_link = True
    readonly_fields= ('intervenant','fonction_de_intervenant')

   
class CustomDemandeEcranAdmin(admin.ModelAdmin):

    inlines= [DemandeEcranInline,OrdinateurInline,]
    search_fields = ['numero_inventaire'] 
    list_filter =  ['etat_de_materiel']
    list_display = ['numero_inventaire','numero_serie','etat_de_materiel_','marque','taille_de_lecran']

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Ecran' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Ecran')
        row_num = 1
        columns = [field.verbose_name for field in meta.fields]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.HAIR
        borders.right = xlwt.Borders.HAIR
        borders.top = xlwt.Borders.HAIR
        borders.bottom = xlwt.Borders.HAIR
        font_style.borders = borders
        font_style.alignment.wrap = 1
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(columns[col_num]), font_style)

        row = []

        for obj in queryset:
            for field in fieldnames:
                if getattr(obj,field) == None:
                    a = ''
                else:
                    a = getattr(obj,field)
                row.append(a)
                if len(row)== len(fieldnames):
                    
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                    row = []
        wb.save(response)
        return response
    export_to_csv.short_description = "Export"
admin.site.register(Ecran,CustomDemandeEcranAdmin)

#===================SErver=================================
class DemandeserveurInline(admin.StackedInline):
    model =DemandeServeur 
    extra = 0
    show_change_link = True
    readonly_fields= ('intervenant','fonction_de_intervenant')




class CustomDemandeserveurAdmin(admin.ModelAdmin):

    inlines= [DemandeserveurInline,]
    search_fields = ['numero_inventaire'] 
    list_filter =  ['etat_de_materiel']
    list_display = ['numero_inventaire','numero_serie','etat_de_materiel_','nom_du_serveur','Employe_que_gerer','processeur','taille_de_disque_dur','ram','system_d_exploitation']
    raw_id_fields = ['Employe_que_gerer']

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Serveur' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Serveur')
        row_num = 1
        columns = [field.verbose_name for field in meta.fields]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.HAIR
        borders.right = xlwt.Borders.HAIR
        borders.top = xlwt.Borders.HAIR
        borders.bottom = xlwt.Borders.HAIR
        font_style.borders = borders
        font_style.alignment.wrap = 1
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, str(columns[col_num]), font_style)

        row = []

        for obj in queryset:
            for field in fieldnames:
                if getattr(obj,field) == None:
                    a = ''
                else:
                    a = getattr(obj,field)
                row.append(a)
                if len(row)== len(fieldnames):
                    
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                    row = []
        wb.save(response)
        return response
    export_to_csv.short_description = "Export"
admin.site.register(Serveur,CustomDemandeserveurAdmin)

 
