from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models.account import Account
from .models.cita import Cita
from .models.especialidad import Especialidad
from .models.medico import Medico
from .models.user import User

admin.site.register(Account)
admin.site.register(Cita)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(User)