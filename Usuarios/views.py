#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from Usuarios.serializers import *

#class UsuarioAPI (viewsets.ModelViewSet):
 #   serializer_class = UserSerial
   # queryset = get_user_model().objects.all()


class perfilAPI (viewsets.ModelViewSet):
    serializer_class = perfilSerial
    queryset = perfil.objects.all()

class docenteAPI (viewsets.ModelViewSet):
    serializer_class = docenteSerial
    queryset = docente.objects.all()

class padreFamiliaAPI (viewsets.ModelViewSet):
    serializer_class = padreFamiliaSerial
    queryset = padreFamilia.objects.all()

class administrativosAPI (viewsets.ModelViewSet):
    serializer_class = administrativosSerial
    queryset = administrativos.objects.all()

class alumnoAPI (viewsets.ModelViewSet):
    serializer_class = alumnoSerial
    queryset = alumno.objects.all()
