from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    exclude = ['asignado']
    list_display = (
       'rut', 'email', 'first_name', 'last_name', 'role', 'asignado', 'fecha_nacimiento', 'direccion', 'telefono'
    )
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'rut', 'email')
    ordering = ('rut',)

    fieldsets = (
        (None, {'fields': ('rut', 'password')}),
        ('Información personal', {
            'fields': (
                'first_name', 'last_name', 'email', 
                'fecha_nacimiento', 'direccion', 'telefono'
            )
        }),
        ('Permisos', {
            'fields': (
                'role', 'groups', 'user_permissions'
            )
        }),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('ADD NEW USER', {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'first_name', 'last_name', 'rut', 'role',
                'fecha_nacimiento', 'direccion', 'telefono', 
            ),
        }),
    )
