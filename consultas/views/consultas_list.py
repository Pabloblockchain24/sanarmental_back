from rest_framework import generics
from consultas.models import Consulta
from consultas.serializers import ConsultasSerializer

class ConsultaListView(generics.ListAPIView):
    queryset = Consulta.objects.all() 
    serializer_class = ConsultasSerializer 