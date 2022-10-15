from rest_framework import serializers
from shsApp.models.cita import Cita

class CitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita
        fields = ['id', 'especialidad', 'user', 'medico', 'fecha_cita', 'hora_cita']   

        

       