from rest_framework import generics

from consultas.models import Consulta
from consultas.serializers import ConsultasSerializer, ConsultasCreateSerializer

class ConsultaCreateView(generics.CreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultasCreateSerializer


class ConsultaDetailView(generics.RetrieveAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultasSerializer
    lookup_field = 'id'

from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class ConsultaDeleteView(generics.DestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultasSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        paciente_nombre = instance.paciente.user.get_full_name()
        paciente_email = instance.paciente.user.email
        profesional_nombre = instance.profesional.user.get_full_name()
        fecha = instance.fecha
        hora = instance.hora
        paciente_rut = instance.paciente.user.rut

        # Eliminamos
        self.perform_destroy(instance)

        # Luego enviamos el correo
        try:
            self.send_cancellation_email(
                paciente_nombre, paciente_email, profesional_nombre, fecha, hora, paciente_rut
            )
        except Exception as e:
            print("Error al enviar correo de cancelación:", e)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def send_cancellation_email(self, paciente_nombre, paciente_email, profesional_nombre, fecha, hora, paciente_rut ):
        subject = "Cancelación de Consulta "
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [paciente_email]

        context = {
            'paciente_nombre': paciente_nombre,
            'profesional_nombre': profesional_nombre,
            'fecha': fecha.strftime('%d-%m-%Y'),  
            'hora': hora.strftime('%H:%M'),       
            'paciente_rut': paciente_rut
        }

        html_message = render_to_string('cancel_consulta.html', context)
        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

 
