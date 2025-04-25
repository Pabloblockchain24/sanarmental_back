from django.urls import path
from api.views.pacientes import PacienteListView, PacienteDetailView

urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='pacientes-list'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),

]