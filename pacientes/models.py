#Importante: las relaciones entre pacientes y consultas, serán solo manejadas desde el modelo consultas
#Para consultar todas las consultas de un paciente, se hará paciente.consulta.all()
from django.db import models
from usuarios.models import CustomUser
class Paciente(models.Model):
    user = models.OneToOneField(
        CustomUser,  
        on_delete=models.CASCADE,
        related_name='paciente',
        limit_choices_to={
            'role': CustomUser.Role.PACIENTE,
            
        },
    )

    sexo = models.CharField(
        'Sexo', max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        null=True, blank=True
    )
    motivo_consulta = models.CharField('Motivo de consulta', max_length=1000, null=True, blank=True)
    objetivos = models.CharField('Objetivos', max_length=1000, null=True, blank=True)

  
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
