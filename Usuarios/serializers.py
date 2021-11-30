#from django.db.models.base import Model
from rest_framework import serializers

from Usuarios.models import *

#class UserSerial (serializers.ModelSerializer):
    #class Meta:
       # model = get_user_model()
       # fields = ['username', 'email', 'password']
       # extra_kwargs = {
            #'password': {
               # 'write_only':True,
                #'style': {
                 #   'input_type': 'password'
                #}
            #}
       # }

class perfilSerial(serializers.ModelSerializer):
    class Meta:
        model = perfil
        fields = '__all__'

class docenteSerial(serializers.ModelSerializer):
    class Meta:
        model = docente
        fields = '__all__'

class padreFamiliaSerial(serializers.ModelSerializer):
    class Meta:
        model = padreFamilia
        fields = '__all__'

class administrativosSerial(serializers.ModelSerializer):
    class Meta:
        model = administrativos
        fields = '__all__'

class alumnoSerial(serializers.ModelSerializer):
    class Meta:
        model = alumno
        fields = '__all__'