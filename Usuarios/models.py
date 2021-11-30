from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model


class perfil (models.Model):
    usuario = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    nombre = models.CharField (max_length=200)
    apellido = models.CharField (max_length=200)
    direccion = models.CharField (max_length=200)
    telefono = models.CharField (max_length=200)
    edad = models.IntegerField (blank=False)

    def __str__(self):
        return self.nombre+' '+self.apellido

class docente (models.Model):
    id= models.IntegerField(primary_key=True)
    nombre= models.ForeignKey(perfil, on_delete=models.CASCADE)
    #asignaturas= models.ManyToManyField(materias)
    asignaturas= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre.__str__()


class administrativos (models.Model):
    id= models.IntegerField(primary_key=True)
    nombre= models.ForeignKey(perfil, on_delete=models.CASCADE)
    cargo= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre+' '+self.cargo

class padreFamilia (models.Model):
    nombre= models.ForeignKey(perfil, on_delete=models.CASCADE)
    # falta crear atributo hijo y relacionarlo

    def __str__(self):
        return self.nombre.__str__()

class alumno (models.Model):
    id= models.IntegerField(primary_key=True)
    nombre = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    padres = models.CharField (max_length=200)
    acudiente = models.CharField (max_length=200)
    grado = models.CharField (max_length=20)

    def __str__(self):
        return self.nombre+' '+self.grado