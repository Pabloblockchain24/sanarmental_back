from django.contrib import admin

from .models import Profesional 

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'rut', 'fecha_nacimiento', 'tipo_atencion', 'especialidad', 'direccion', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'rut', 'especialidad')
    list_filter = ('tipo_atencion', 'especialidad')
    list_per_page = 10
    ordering = ('apellido',)