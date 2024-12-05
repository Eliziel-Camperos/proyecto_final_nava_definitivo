from django.urls import path
from inventario_app import views

urlpatterns = [
    path('Inventario/',views.index_Inventario,name='Inventario'),
    path('regisInv/',views.regisInv,name='regisInv'),
    path('selecInv/<id>',views.selecInv,name="selecInv"),
    path('editInv/',views.editInv,name="editInv"),
    path('borrarInv/<id>',views.borrarInv,name="borrarInv"),
]