from django.db import models
from .especialidad import Especialidad
from .user import User
from .medico import Medico

class Cita(models.Model):
    
    id = models.AutoField(primary_key=True)
    especialidad = models.ForeignKey(Especialidad, related_name='Name', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='DNI', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name='DNI', on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()