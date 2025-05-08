from rest_framework import generics
from profesionales.models import Profesional
from sanarmental_back.shared_serializers import ProfesionalSerializer


#ListAPIView is a generic view from DRF that provides a read-only endpoint to list a queryset.
class ProfesionalListView(generics.ListAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
