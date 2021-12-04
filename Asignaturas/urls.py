from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Asignaturas.views import *

router = DefaultRouter()
router.register('materias', materiasAPI)
router.register('notas', notasAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]