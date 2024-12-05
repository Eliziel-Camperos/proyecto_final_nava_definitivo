from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Venta',views.index_Venta,name='Venta'),
    path('regisVen/',views.regisVenta,name='regisVen'),
    path('selecVen/<id>',views.selecVen,name="selecVen"),
    path('editVen/',views.editVen,name="editVen"),
    path('borrarVen/<id>',views.borrarVen,name="borrarVen"),
]           