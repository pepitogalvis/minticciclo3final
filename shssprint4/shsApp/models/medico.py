from django.db import models
from .especialidad import Especialidad

class Medico(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name',max_length = 50)
    last_name = models.CharField('Last_Name',max_length = 50, null=False)
    phone = models.CharField('Phone',max_length = 10,null=False)
    especialidad_medico = models.ForeignKey(Especialidad, related_name='Tiene_Especialidad', on_delete=models.CASCADE)
    tarjeta_profesional = models.CharField('TP',max_length = 30, null=False)
    documento_medico = models.CharField('DNI', max_length = 50, unique=True)