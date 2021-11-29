from django.contrib import admin
from .models import Paciente, Tessiu

# Registra tus modelos aqui.
#------------------------------------------------------------
#nuevo forma de registro 
#@admin.register()    <-- esto es un decorador
#class Admin(admin.ModelAdmin):
#    '''Admin View for '''

#    list_display = ('',)
#    list_filter = ('',)   <-- Esto es para generar filtros
#    inlines = [
#        Inline,
#    ]
#    raw_id_fields = ('',)
#    readonly_fields = ('',)  <--Campos de solo lectura
#    search_fields = ('',)  <--Sirve para hacer busquedas
#    date_hierarchy = ''
#    ordering = ('',)  <-- Ordenar los campos (- es para mayor a menor) y si no se pone el valor de menos sera de forma creciente 
#--------------------------------------------------------------
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)
#----------------------------------------------------------------
#Aque se registra el modelo por ejemplo "Tessiu"
class TessiuAdmin(admin.ModelAdmin):
    #Aqui se muestra cuantos campos quiero que se despliegen:
    list_display = ('Color','Temperatura','inflammation','name')
    #Ejemplo de filtrar por color
    list_filter = ('Color','name')
    #Ejemplo de campo de solo lectura Color
    #readonly_fields = ('Color',)

admin.site.register(Tessiu, TessiuAdmin)
#-------------------------------------------------------------
