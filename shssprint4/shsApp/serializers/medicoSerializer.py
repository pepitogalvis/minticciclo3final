from shsApp.models.medico import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medico
        fields = ['name', 'last_name', 'phone', 'especialidad_medico', 'tarjeta_profesional', 'documento_medico']

       
   