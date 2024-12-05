from django.db import models

# Create your models here.

class Empleado(models.Model):
    id_empleado=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=100)
    apellido=models.CharField( max_length=100)
    numero=models.IntegerField(max_length=10)
    sexo=models.CharField( max_length=50)
    puesto=models.CharField( max_length=50)
    salario=models.FloatField()
    direccion=models.CharField( max_length=150)
    
    def __str__(self):
        return self.nombre