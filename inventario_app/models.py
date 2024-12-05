from django.db import models

# Create your models here.

class Inventario(models.Model):
    id_inven=models.IntegerField(primary_key=True)
    id_comic=models.IntegerField()
    cantidad_dispo=models.IntegerField()
    ubicacion=models.CharField( max_length=250)
    fecha_entrada=models.DateField( auto_now=False, auto_now_add=False)
    estado=models.CharField( max_length=50)
    id_tienda=models.IntegerField()
    def __str__(self):
        return self.id_inven 