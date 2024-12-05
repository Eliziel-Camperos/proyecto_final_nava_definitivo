from django.db import models

# Create your models here.

class Devolucion(models.Model):
    id_devo=models.IntegerField(primary_key=True)
    id_venta=models.IntegerField()
    id_comic=models.IntegerField()
    fecha_devo=models.DateField( auto_now=False, auto_now_add=False)
    motivo=models.CharField( max_length=250)
    cantidad=models.IntegerField()
    estado=models.CharField( max_length=50)
    def __str__(self):
        return self.id_devo