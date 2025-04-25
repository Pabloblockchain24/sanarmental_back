from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pacientes.models import Paciente
from api.serializers import PacienteSerializer


class PacienteListView(APIView):
    def get(self, request):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)


class PacienteDetailView(APIView):
   def get(self, request, pk):
        try:
            paciente = Paciente.objects.get(pk=pk)
            serializer = PacienteSerializer(paciente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Paciente.DoesNotExist:
            return Response({'detail': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)