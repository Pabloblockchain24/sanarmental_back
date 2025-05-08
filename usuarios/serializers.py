from rest_framework import serializers
from usuarios.models import CustomUser 

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'rut', 'fecha_nacimiento', 'direccion', 'telefono']

    def validate_rut(self, value):
        print('💣💣💣Entre al validate_rut')
        # Verificar si el RUT ya está en uso
        if CustomUser.objects.filter(rut=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Ya existe usuario con este Rut.")
        return value