#Importante: las relaciones entre pacientes y consultas, serán solo manejadas desde el modelo consultas
#Para consultar todas las consultas de un paciente, se hará paciente.consulta.all()
from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    rut = models.CharField('Rut', max_length=20)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=10, choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ], default='O', null=True, blank=True)
    direccion = models.CharField('Direccion', max_length=200, null=True, blank=True)
    telefono = models.CharField('Telefono contacto:', max_length=20)
    correo = models.EmailField('Correo', max_length=100)
    imagen = models.ImageField(upload_to='pacientes/imgs/', null=True, blank=True)
    motivo_consulta = models.CharField('Motivo de consulta', max_length=1000, null=True, blank=True)
    objetivos = models.CharField('Objetivos', max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"