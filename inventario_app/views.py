from django.shortcuts import render,redirect
from .models import Inventario
# Create your views here.
def index_Inventario(request):
    nInventario=Inventario.objects.all()
    return render(request,'gestInv.html',{'mInventario':nInventario})

def regisInv(request): 
    inven=request.POST["txtinv"]
    com=request.POST["txtcom"]
    can=request.POST["txtcan"]
    ubi=request.POST["txtubi"]
    fec=request.POST["fec"]
    est=request.POST["txtest"]
    tie=request.POST["numtie"]

    guarInven=Inventario.objects.create(
            id_inven=inven,id_comic=com,cantidad_dispo=can,ubicacion=ubi,fecha_entrada=fec,estado=est,id_tienda=tie
    )
    return redirect("Inventario")

def selecInv(request,id):
    ven=Inventario.objects.get(id_inven=id)
    return render(request,'editarInv.html',{"mInventario":ven})

def editInv(request):
    inv=request.POST["txtinv"]
    com=request.POST["txtcom"]
    can=request.POST["txtcan"]
    fec=request.POST["fec"]
    ubi=request.POST["txtubi"]
    ext=request.POST["txtest"]
    tie=request.POST["numtie"]
    inven=Inventario.objects.get(id_inven=inv)
    inven.id_comic=com
    inven.cantidad_dispo=can
    inven.ubicacion=ubi 
    inven.fecha_entrada=fec
    inven.estado=ext
    inven.id_tienda=tie
    inven.save()
    return redirect('Inventario')

def borrarInv(request,id):
    inven=Inventario.objects.get(id_inven=id)
    inven.delete()
    return redirect('Inventario')
