from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Asignaturas.serializers import *

class materiasAPI (viewsets.ModelViewSet):
    serializer_class = materiasSerial
    queryset = materias.objects.all()

class notasAPI (viewsets.ModelViewSet):
    serializer_class = notasSerial
    queryset = notas.objects.all()