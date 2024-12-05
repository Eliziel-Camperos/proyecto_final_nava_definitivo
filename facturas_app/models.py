from django.db import models

# Create your models here.
class Factura(models.Model):
    id_factura=models.IntegerField(primary_key=True)
    id_venta=models.IntegerField()
    fecha_fac=models.DateField(auto_now=False, auto_now_add=False)
    total=models.FloatField()
    metodo_pago=models.CharField(max_length=50)
    id_cliente=models.IntegerField()
    descuento=models.IntegerField()
    def __str__(self):
        return self.id_factura