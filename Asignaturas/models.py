from django.db import models
from Usuarios.models import docente

# Create your models here.

class materias (models.Model):
    nombre = models.CharField (max_length=200)
    area = models.CharField (max_length=200)
    grado = models.CharField (max_length=200)
    profesor = models.ForeignKey (docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+' '+self.grado+' '+self.area


class notas (models.Model):
    materia = models.ForeignKey (materias, on_delete=models.CASCADE)
    cuantitativa = models.FloatField(default=0)
    cualitativa = models.CharField (max_length=200)
    estudiante = models.CharField

    def __str__(self):
        return self.materia+' '+self.cuantitativa