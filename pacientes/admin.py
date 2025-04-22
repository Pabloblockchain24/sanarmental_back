from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Paciente 

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'rut', 'fecha_nacimiento', 'sexo', 'direccion', 'telefono', 'correo')  
    list_per_page = 10
    ordering = ('apellido', 'nombre')

