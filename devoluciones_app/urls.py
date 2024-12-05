from django.urls import path
from devoluciones_app import views

urlpatterns = [
    path('Devolucion/',views.index_dev,name='Devolucion'),
    path('regisDev/',views.regisDev,name='regisDev'),
    path('selecDev/<id>',views.selecDev,name="selecDev"),
    path('editDev/',views.editDev,name="editDev"),
    path('borrarDev/<id>',views.borrarDev,name="borrarDev"),
]