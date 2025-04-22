#Importante: las relaciones entre profesionales y consultas, serán solo manejadas desde el modelo consultas
#Para consultar todas las consultas de un profesional, se hará profesional.consulta.all()
from django.db import models

class Profesional(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    rut = models.CharField('Rut', max_length=20)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    tipo_atencion = models.CharField('Tipo de Atencion',choices=[('Presencial', 'Presencial'), ('Online', 'Online')], max_length=255, null=True, blank=True)
    especialidad = models.CharField('Especialidad', max_length=100, null=True, blank=True)
    direccion = models.CharField('Direccion', max_length=200, null=True, blank=True)
    telefono = models.CharField('Telefono contacto:', max_length=20)
    correo = models.EmailField('Correo', max_length=100)
    imagen = models.ImageField(upload_to='profesionales/imgs/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"