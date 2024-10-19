import csv
from ctypes import alignment
from datetime import datetime
from tkinter import font
from urllib.request import ProxyBasicAuthHandler
from django.contrib import admin
from django.http import HttpResponse
from .models import DemandeOrdinateur,DemandeScanner,DemandeEcran,DemandeImprimante,DemandeServeur
from django.contrib.auth import get_user_model
import xlwt


#===================DemandeOrdinateur=================================


class CustomordinateurDemandeAdmin(admin.ModelAdmin):
    raw_id_fields=['ordinateur']
    search_fields = ['ordinateur__numero_inventaire'] 
    list_display = ['ordinateur','intervenant','fonction_de_intervenant','Nature_de_la_panne']

    readonly_fields= ('intervenant','fonction_de_intervenant')

    def save_model(self, request, obj, form, change):
        #for get tier mail
        if obj.intervenant == None:
            obj.intervenant=request.user.last_name + " " + request.user.first_name
            obj.fonction_de_intervenant = request.user.Fonction_de_user
            super().save_model(request, obj, form, change)
    
    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Demande Ordinateur' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Demande Odinateur')
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

admin.site.register(DemandeOrdinateur,CustomordinateurDemandeAdmin)

#===================DemandeScanner=================================
 
class DemandeScannerCustomModelAdmin(admin.ModelAdmin):

    raw_id_fields=['Scanner']
    search_fields = ['Scanner__numero_inventaire'] 
    list_display = ['code_bar','Scanner','intervenant','fonction_de_intervenant','Nature_de_la_panne']
    readonly_fields= ('intervenant','fonction_de_intervenant')
    def save_model(self, request, obj, form, change):
        #for get tier mail
        if obj.intervenant == None:
            obj.intervenant=request.user.last_name + " " + request.user.first_name
            obj.fonction_de_intervenant = request.user.Fonction_de_user
            super().save_model(request, obj, form, change)


    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Demande Scanner' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('DemandeScanner')
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
admin.site.register(DemandeScanner,DemandeScannerCustomModelAdmin)

#===================Demandeimprimante=================================
 
class DemandeImprimanteCustomModelAdmin(admin.ModelAdmin):

    raw_id_fields=['Imprimante']
    search_fields = ['Imprimante__numero_inventaire'] 
    list_display = ['code_bar','Imprimante','intervenant','fonction_de_intervenant','Nature_de_la_panne']
    readonly_fields= ('intervenant','fonction_de_intervenant')
    def save_model(self, request, obj, form, change):
        #for get tier mail
        if obj.intervenant == None:
            obj.intervenant=request.user.last_name + " " + request.user.first_name
            obj.fonction_de_intervenant = request.user.Fonction_de_user
            super().save_model(request, obj, form, change)
    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Demande Imprimante' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('DemandeImprimante')
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
admin.site.register(DemandeImprimante,DemandeImprimanteCustomModelAdmin)

#===================Demandeecran=================================
 
class DemandeEcranCustomModelAdmin(admin.ModelAdmin):

    raw_id_fields=['Ecran']
    search_fields = ['Ecran__numero_inventaire'] 
    list_display = ['code_bar','Ecran','intervenant','fonction_de_intervenant','Nature_de_la_panne']
    readonly_fields= ('intervenant','fonction_de_intervenant')
    def save_model(self, request, obj, form, change):
        #for get tier mail
        if obj.intervenant == None:
            obj.intervenant=request.user.last_name + " " + request.user.first_name
            obj.fonction_de_intervenant = request.user.Fonction_de_user
            super().save_model(request, obj, form, change)

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Demande Ecran' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('DemandeEcran')
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

admin.site.register(DemandeEcran,DemandeEcranCustomModelAdmin)

#===================Demandeecran=================================
 
class DemandeServeurCustomModelAdmin(admin.ModelAdmin):

    raw_id_fields=['Serveur']
    search_fields = ['Serveur__numero_inventaire'] 
    list_display = ['code_bar','Serveur','intervenant','fonction_de_intervenant','Nature_de_la_panne']

    readonly_fields= ('intervenant','fonction_de_intervenant')
    def save_model(self, request, obj, form, change):
        #for get tier mail
        if obj.intervenant == None:
            obj.intervenant=request.user.last_name + " " + request.user.first_name
            obj.fonction_de_intervenant = request.user.Fonction_de_user
            super().save_model(request, obj, form, change)

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Demande Serveur' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('DemandeServeur')
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


admin.site.register(DemandeServeur,DemandeServeurCustomModelAdmin)



 