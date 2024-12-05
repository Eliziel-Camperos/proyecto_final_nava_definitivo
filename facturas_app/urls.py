from django.urls import path
from facturas_app import views

urlpatterns = [
    path('Facturas/',views.index_facturas,name='Facturas'),
    path('regisFac/',views.regisFac,name='regisFac'),
    path('selecfac/<int:id>',views.selecfac,name="selecfac"),
    path('editfac/',views.editfac,name="editfac"),
    path('borrarfac/<id>',views.borrarfac,name="borrarfac"),
]