from django.shortcuts import render,redirect
from .models import Tienda
# Create your views here.

def index_Tienda(request):
    nTienda=Tienda.objects.all()
    return render(request,'gestien.html',{'mTienda':nTienda})

def regisTienda(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direc=request.POST["txtdir"]
    numero=request.POST["num"]
    correo=request.POST["txtcor"]
    horario=request.POST["txthor"]
    
    
    guarTienda=Tienda.objects.create(
            id_tienda=id,nombre=nombre,horario=horario,telefono=numero,coreo_elec=correo,direccion=direc
    )
    return redirect("Tienda")

def selecTie(request,id):
    tie=Tienda.objects.get(id_tienda=id)
    return render(request,'editarTie.html',{"mTienda":tie})

def editTie(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    direc=request.POST["txtdir"]
    numero=request.POST["num"]
    correo=request.POST["txtcor"]
    horario=request.POST["txthor"]
    tie=Tienda.objects.get(id_tienda=id)
    tie.nombre=nombre
    tie.telefono=numero
    tie.coreo_elec=correo
    tie.direccion=direc 
    tie.horario=horario
    tie.save()
    return redirect('Tienda')

def borrarTie(request,id):
    tie=Tienda.objects.get(id_tienda=id)
    tie.delete()
    return redirect('Tienda')