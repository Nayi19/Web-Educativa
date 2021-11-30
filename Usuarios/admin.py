from django.contrib import admin

# Register your models here.

from Usuarios.models import *

admin.site.register(perfil)
admin.site.register(docente)
admin.site.register(padreFamilia)
admin.site.register(alumno)
admin.site.register(administrativos)