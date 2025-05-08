from django.urls import path
from .views import (
    PacienteDetailView, 
    PacienteListView, 
    PacienteConsultasView, 
    PacienteCreateView,
    # PacienteUpdateView,
    PacienteDeleteView
    )

urlpatterns = [
    path('', PacienteListView.as_view(), name='lista_pacientes'),
    path('nuevo_paciente/', PacienteCreateView.as_view(), name='nuevo_paciente'),   
    path('<str:rut>/', PacienteDetailView.as_view(), name='detalles_paciente'),
    # path('<str:rut>/editar/', PacienteUpdateView.as_view(), name='editar_paciente'),
    path('<str:rut>/eliminar/', PacienteDeleteView.as_view(), name='eliminar_paciente'),
    path('<str:rut>/consultas/', PacienteConsultasView.as_view(), name='consultas_paciente')
]