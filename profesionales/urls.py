from django.urls import path
from .views import (
    ProfesionalListView, 
    ProfesionalDetailView, 
    ProfesionalCreateView,
    # ProfesionalUpdateView,
    ProfesionalDeleteView,
    ProfesionalConsultasDetailView, 
    ProfesionalDisponibilidadDetailView
)


urlpatterns = [
    path('', ProfesionalListView.as_view(), name='lista_profesionales'),
    # path('<str:user__rut>/editar/', ProfesionalUpdateView.as_view(), name='editar_profesional'),
    path('nuevo_profesional/', ProfesionalCreateView.as_view(), name='nuevo_profesional'),   
    path('<str:rut>/eliminar/', ProfesionalDeleteView.as_view(), name='eliminar_profesional'),
    path('<str:rut>/consultas/', ProfesionalConsultasDetailView.as_view(), name='profesional_consultas' ),
    path('<str:rut>/disponibilidad/', ProfesionalDisponibilidadDetailView.as_view(), name='disponibilidad_profesional'),
    path('<str:rut>/', ProfesionalDetailView.as_view(), name='detalles_profesional'),
]