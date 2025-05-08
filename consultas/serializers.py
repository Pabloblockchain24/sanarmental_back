from rest_framework import serializers, viewsets, status
from consultas.models import Consulta
from profesionales.models import Profesional
from pacientes.models import Paciente
from sanarmental_back.shared_serializers import ProfesionalSerializer, PacienteSerializer
from rest_framework.response import Response

class ConsultasSerializer(serializers.ModelSerializer):
    profesional = ProfesionalSerializer(read_only=True)
    paciente = PacienteSerializer(read_only=True)

    class Meta:
        model = Consulta
        fields = '__all__'

class ConsultasDetailProfesionalSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'hora', 'estado', 'paciente']

class ConsultasDetailPacienteSerializer(serializers.ModelSerializer):
    profesional = serializers.SerializerMethodField()

    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'hora', 'estado', 'profesional' ]

    def get_profesional(self, obj):
        return {
            'name': obj.profesional.user.first_name if obj.profesional and obj.profesional.user else '',
            'lastname': obj.profesional.user.last_name if obj.profesional and obj.profesional.user else '',
            'rut': obj.profesional.user.rut if obj.profesional and obj.profesional.user else '',
        }    


class ConsultaDisponibilidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'hora']

import threading
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

class ConsultasCreateSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(write_only=True)
    profesional = serializers.CharField(write_only=True)

    class Meta:
        model = Consulta
        fields = '__all__'

    def create(self, validated_data):
        paciente_rut = validated_data.pop('paciente')
        profesional_rut = validated_data.pop('profesional')

        try:
            profesional = Profesional.objects.get(user__rut=profesional_rut)
        except Profesional.DoesNotExist:
            raise serializers.ValidationError({'profesional': 'Profesional no encontrado.'})
        
        try:
            paciente = Paciente.objects.get(user__rut=paciente_rut)
        except Paciente.DoesNotExist:
            raise serializers.ValidationError({'paciente': 'Paciente no encontrado.'})

        consulta = Consulta.objects.create(paciente=paciente, profesional=profesional, **validated_data)

        try:
            self.send_notification_email(consulta)
        except Exception as e:
         raise serializers.ValidationError({"error": "Hubo un problema al enviar correo de confirmación."})

        return consulta

    def send_notification_email(self, consulta):
        def send_email():
            subject = '¡Consulta confirmada!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to = [consulta.paciente.user.email]

            context = {
                'paciente_nombre': consulta.paciente.user.get_full_name(),
                'profesional_nombre': consulta.profesional.user.get_full_name(),
                'fecha': consulta.fecha,
                'hora': consulta.hora,
                'estado': consulta.estado,
                'paciente_rut': consulta.paciente.user.rut
            }

            text_content = f'Nueva consulta creada entre {context["paciente_nombre"]} y {context["profesional_nombre"]}.'
            html_content = render_to_string('new_consulta.html', context)

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        threading.Thread(target=send_email).start()