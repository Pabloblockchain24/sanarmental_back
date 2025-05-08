from django.urls import path
from .views import ConsultaListView, ConsultaDetailView, ConsultaCreateView, ConsultaDeleteView

urlpatterns = [
    path('', ConsultaListView.as_view(), name='lista_consultas'), 
    path('nueva_consulta/', ConsultaCreateView.as_view(), name='nueva_consulta'),
    path('<str:id>/eliminar/', ConsultaDeleteView.as_view(), name='eliminar_consulta'),
    path('<str:id>/', ConsultaDetailView.as_view(), name='detalles_consulta'),
]