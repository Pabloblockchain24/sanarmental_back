from rest_framework import generics
from pacientes.models import Paciente
from consultas.models import Consulta
from sanarmental_back.shared_serializers import PacienteSerializer 
from consultas.serializers import ConsultasDetailPacienteSerializer
from django.shortcuts import get_object_or_404

class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'user__rut'

    def get_object(self):
        rut = self.kwargs['rut']
        return get_object_or_404(Paciente, user__rut=rut)
    

class PacienteConsultasView(generics.ListAPIView):
    serializer_class = ConsultasDetailPacienteSerializer

    def get_queryset(self):
        rut = self.kwargs['rut']
        paciente = get_object_or_404(Paciente, user__rut=rut)
        return Consulta.objects.filter(paciente=paciente).exclude(estado__in=['Cancelada'])
    
class PacienteCreateView(generics.CreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer



class PacienteDeleteView(generics.DestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'user__rut'

    def get_object(self):
        rut = self.kwargs['rut']
        return get_object_or_404(Paciente, user__rut=rut)
    
# class PacienteUpdateView(generics.UpdateAPIView):
#     queryset = Paciente.objects.all()
#     serializer_class = PacienteSerializer
#     # lookup_field = 'user__rut'

#     def get_object(self):
#         rut = self.kwargs.get('rut')  # viene de la URL
#         paciente = get_object_or_404(Paciente, user__rut=rut)  # buscas por el RUT del usuario
#         return paciente
    
#     def put(self, request, *args, **kwargs):
#         print(request.data)  # <-- agrega esto
#         return super().put(request, *args, **kwargs)
