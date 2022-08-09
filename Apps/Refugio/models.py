from django.db import models

# Create your models here.


class Refugio (models.Model):

    nombre = models.CharField(max_length= 50, unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    direccion = models.TextField(max_length=100) 

    def __str__(self):
        return f" {self.nombre} - {self.telefono} - {self.email} - {self.direccion}"

