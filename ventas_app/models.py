from django.db import models

# Create your models here.
class Venta(models.Model):
    id_tienda=models.IntegerField(primary_key=True)
    id_comic=models.IntegerField()
    id_empleado=models.IntegerField()
    fecha_venta=models.DateField( auto_now=False, auto_now_add=False)
    Cant_comic=models.IntegerField()
    total=models.FloatField()
    def __str__(self):
        return self.Cant_comic  