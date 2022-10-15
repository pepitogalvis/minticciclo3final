from shsApp.models.especialidad import Especialidad
from rest_framework import serializers

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['especialidad_nombre']
    