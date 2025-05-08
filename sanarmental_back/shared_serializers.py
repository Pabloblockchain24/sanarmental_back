from rest_framework import serializers
from usuarios.models import CustomUser
from profesionales.models import Profesional 
from pacientes.models import Paciente
from consultas.models import Consulta
from usuarios.serializers import CustomUserSerializer

# Serializer pequeño para mostrar las consultas dentro de Profesional
class ConsultaProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'hora', 'estado', 'paciente']

# Serializer pequeño para mostrar las consultas dentro de Paciente
class ConsultaPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'hora', 'estado', 'profesional']

class ProfesionalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    consultas = ConsultaProfesionalSerializer(many=True, read_only=True)
    disponibilidad = serializers.SerializerMethodField()

    class Meta:
        model = Profesional
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user  # El User asociado al Profesional
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            user_instance.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.get('rut')
        user = CustomUser.objects.create_user(
            username=username,
            **user_data,
            role=CustomUser.Role.PROFESIONAL
        )
        profesional = Profesional.objects.create(user=user, **validated_data)
        return profesional
    
    def get_disponibilidad(self, obj):
        consultas = Consulta.objects.filter(profesional=obj, estado__in=['Creada', 'Cancelada'])
        return ConsultaProfesionalSerializer(consultas, many=True).data

class PacienteSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    consultas = ConsultaPacienteSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = ['id',  'sexo', 'motivo_consulta', 'objetivos', 'consultas', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.get('rut')
        user = CustomUser.objects.create_user(
            username=username,
            **user_data,
            role=CustomUser.Role.PACIENTE
        )
        paciente = Paciente.objects.create(user=user, **validated_data)
        return paciente

class ConsultaDisponibilidadSerializer(serializers.ModelSerializer):
    pass