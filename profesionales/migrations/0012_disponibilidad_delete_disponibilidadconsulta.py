# Generated by Django 5.1.4 on 2025-04-26 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0011_disponibilidadconsulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('disponible', models.BooleanField(default=False)),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disponibilidad', to='profesionales.profesional')),
            ],
            options={
                'unique_together': {('profesional', 'fecha', 'hora')},
            },
        ),
        migrations.DeleteModel(
            name='DisponibilidadConsulta',
        ),
    ]
