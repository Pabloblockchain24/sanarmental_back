from rest_framework import generics
from profesionales.models import Profesional
from consultas.models import Consulta
from sanarmental_back.shared_serializers import ProfesionalSerializer, ConsultaDisponibilidadSerializer
from consultas.serializers import ConsultasSerializer, ConsultasDetailProfesionalSerializer, ConsultaDisponibilidadSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


# RetrieveAPIView es una vista genérica de DRF para obtener un solo objeto.
class ProfesionalDetailView(generics.RetrieveAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    lookup_field = 'user__rut'

    def get_object(self):
        rut = self.kwargs['rut']
        return get_object_or_404(Profesional, user__rut=rut)


class ProfesionalCreateView(generics.CreateAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


# class ProfesionalUpdateView(generics.UpdateAPIView):
#     queryset = Profesional.objects.all()
#     serializer_class = ProfesionalSerializer
#     lookup_field = 'user__rut'

#     def update(self, request, *args, **kwargs):
#         profesional_instance = self.get_object()
#         print('💣💣Profesional', profesional_instance)

#        ## en request.data viene lo que trae el body
#         print('💣💣request.data',request.data )
#         try:
#             # Llamamos al super() para que el serializer haga el trabajo de actualizar
#             return super().update(request, *args, **kwargs)

#         except ValidationError as e:
#             print('Entre al validationerror') 
#             return Response(
#                 {"user": {"rut": e.detail}},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

class ProfesionalDeleteView(generics.DestroyAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    lookup_field = 'user__rut'

    def get_object(self):
        rut = self.kwargs['rut']
        return get_object_or_404(Profesional, user__rut=rut)

class ProfesionalConsultasDetailView(generics.ListAPIView):
    serializer_class = ConsultasDetailProfesionalSerializer

    def get_queryset(self):
        rut = self.kwargs['rut']
        profesional = get_object_or_404(Profesional, user__rut=rut)
        return Consulta.objects.filter(profesional=profesional).exclude(estado__in=['Creada', 'Cancelada'])
    
class ProfesionalDisponibilidadDetailView(generics.ListAPIView):
    serializer_class = ConsultaDisponibilidadSerializer

    def get_queryset(self):
        rut = self.kwargs['rut']
        profesional = get_object_or_404(Profesional, user__rut=rut)
        return Consulta.objects.filter(profesional=profesional, estado__in=['Creada', 'Cancelada'])
