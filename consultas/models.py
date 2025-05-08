from django.db import models

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', null=True, blank=True)
    hora = models.TimeField('Hora', null=True, blank=True)
    estado = models.CharField(
        'Estado',
        choices=[
            ('Completada', 'Completada'),
            ('Cancelada', 'Cancelada'),
            ('Agendada', 'Agendada'),
            ('Confirmada', 'Confirmada'),
            ('Creada', 'Creada')  # Estado añadido
        ],
        max_length=255,
        default='Creada',  # El nuevo estado por defecto será 'Creada'
        null=True,
        blank=True
    )
    evolucion = models.CharField('Evolución', max_length=1000, null=True, blank=True)

    profesional = models.ForeignKey('profesionales.Profesional', on_delete=models.SET_NULL, null=True, blank=True, related_name='consultas')
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.SET_NULL, null=True, blank=True, related_name='consultas')
    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} - {self.fecha} - {self.hora}"