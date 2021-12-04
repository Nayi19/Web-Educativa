from rest_framework import serializers

from Asignaturas.models import *

class materiasSerial(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = '__all__'

class notasSerial(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = '__all__'