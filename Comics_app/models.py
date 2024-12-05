from django.db import models

# Create your models here.
class Comics(models.Model):
    id_comics=models.IntegerField(primary_key=True)
    nombre=models.CharField( max_length=250)
    categoria=models.CharField( max_length=50)
    autor=models.CharField( max_length=50)
    serie=models.CharField( max_length=50)
    precio=models.FloatField()
    
    def __str__(self):
        return self.nombre