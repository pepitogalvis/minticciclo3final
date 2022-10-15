from django.db import models

class Especialidad(models.Model):
    
    especialidad_id = models.BigAutoField(primary_key=True)
    especialidad_nombre = models.CharField('Name', max_length = 30, unique=True)