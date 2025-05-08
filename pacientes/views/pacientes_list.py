from rest_framework import generics
from pacientes.models import Paciente
from sanarmental_back.shared_serializers import PacienteSerializer

class PacienteListView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
