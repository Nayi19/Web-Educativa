from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Usuarios.views import *

router = DefaultRouter()
router.register('perfil', perfilAPI)
router.register('docente', docenteAPI)
router.register('padreFamilia', padreFamiliaAPI)
router.register('administrativos', administrativosAPI)
router.register('alumno', alumnoAPI)


urlpatterns = [
    path('crud/', include(router.urls))
]