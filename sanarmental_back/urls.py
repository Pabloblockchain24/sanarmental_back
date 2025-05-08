from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profesionales/', include('profesionales.urls')),
    path('api/consultas/', include('consultas.urls')),
    path('api/pacientes/', include('pacientes.urls')),
]