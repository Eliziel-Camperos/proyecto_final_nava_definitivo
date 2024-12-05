from django.urls import path
from Comics_app import views

urlpatterns = [
    path('Comics',views.index_Comic,name='Comics'),
    path('regisComics/',views.regisComics,name='regisComics'),
    path('selecCom/<id>',views.selecCom,name="selecCom"),
    path('editCom/',views.editCom,name="editCom"),
    path('borrarCom/<id>',views.borrarCom,name="borrarCom"),
]