from sys import modules
from tkinter import SE
from django.contrib import admin
from .models import Employe
from material.models import Ordinateur,Serveur
from datetime import datetime
from ctypes import alignment
from django.http import HttpResponse
import xlwt

# Register your models here.

class OrdinateurInline(admin.StackedInline):
    model=Ordinateur 
    fields = ('numero_inventaire','numero_serie','etat_de_materiel_')
    readonly_fields = fields
    extra = 0
    can_delete = False
    show_change_link = True
    max_num=0
    def has_add_permission(self, request, obj=None):
        return False
class ServeurInline(admin.StackedInline):
    model=Serveur 
    fields = ('numero_inventaire','nom_du_serveur','numero_serie','etat_de_materiel_')
    readonly_fields = fields
    extra = 0
    can_delete = False
    show_change_link = True
    max_num=0
    def has_add_permission(self, request, obj=None):
        return False
class EmployeCustomAdmin(admin.ModelAdmin):
    inlines = [
        OrdinateurInline,ServeurInline
    ]
    search_fields = ['nom','prenom','addresse_ip'] 
    list_display= ['nom','prenom','addresse_ip','Nbureau','direction','fonction']

    actions = ["export_to_csv"]

    def export_to_csv(self,request,queryset):

        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition']='attachment; filename=Employés' + \
                str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Employés')
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
admin.site.register(Employe,EmployeCustomAdmin)