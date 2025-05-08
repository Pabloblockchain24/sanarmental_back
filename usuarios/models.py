from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        PROFESIONAL = 'PROF', 'Profesional'
        PACIENTE = 'PAC', 'Paciente'

    role = models.CharField(max_length=5, choices=Role.choices, default=Role.PACIENTE)
    rut = models.CharField('Rut', max_length=20, unique=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=200, null=True, blank=True)
    telefono = models.CharField('Teléfono de contacto', max_length=20, null=True, blank=True)
    asignado = models.BooleanField('Asignado', null=True, default=False)

    groups = models.ManyToManyField(
        Group, 
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name='customuser_permission_set', 
        blank=True
    )

    def is_paciente(self):
        return self.role == self.Role.PACIENTE

    def is_profesional(self):
        return self.role == self.Role.PROFESIONAL
    
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    def save(self, *args, **kwargs):
        self.username = self.rut
        super().save(*args, **kwargs)
          
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rut}"
