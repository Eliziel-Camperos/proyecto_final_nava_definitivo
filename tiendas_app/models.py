from django.db import models

# Create your models here.
class Tienda(models.Model):
    id_tienda=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=50)
    direccion=models.CharField( max_length=250)
    telefono=models.IntegerField(max_length=10)
    coreo_elec=models.CharField( max_length=150)
    horario=models.CharField( max_length=50)
    
    def __str__(self):
        return self.nombre