from django.contrib import admin
from .models import Profesional 
@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'tipo_atencion', 'especialidad')

