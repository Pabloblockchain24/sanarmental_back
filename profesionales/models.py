#Importante: las relaciones entre profesionales y consultas, serán solo manejadas desde el modelo consultas
#Para consultar todas las consultas de un profesional, se hará profesional.consulta.all()

from django.db import models
from usuarios.models import CustomUser
class Profesional(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profesional',
        limit_choices_to={
            'role': CustomUser.Role.PROFESIONAL,
            'asignado': False
            },
    )

    tipo_atencion = models.CharField(
        'Tipo de Atención',
        choices=[('Presencial', 'Presencial'), ('Online', 'Online')],
        max_length=20, null=True, blank=True
    )
    especialidad = models.CharField('Especialidad', max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"  

    def save(self, *args, **kwargs):
        self.user.asignado = True
        self.user.save()
        super().save(*args, **kwargs)

  
