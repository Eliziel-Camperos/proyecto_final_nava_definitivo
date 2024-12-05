from django.urls import path
from tiendas_app import views

urlpatterns = [
    path('Tienda',views.index_Tienda,name='Tienda'),
    path('regisTienda/',views.regisTienda,name='regisTienda'),
    path('selecTie/<id>',views.selecTie,name="selecTie"),
    path('editTie/',views.editTie,name="editTie"),
    path('borrarTie/<id>',views.borrarTie,name="borrarTie"),
]