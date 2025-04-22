from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Consulta 

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora',  'paciente', 'profesional', 'estado', 'evolucion',)
    list_per_page = 10
    ordering = ('fecha', 'hora')
    formfield_overrides = {
        models.CharField: {
            'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 5, 'cols': 60}),
        },
    }
