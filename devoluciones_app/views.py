from django.shortcuts import render,redirect
from .models import Devolucion

# Create your views here.

def index_dev(request):
    dev=Devolucion.objects.all()
    return render(request,'gestdev.html',{'ndev':dev})

def regisDev(request):
    dev=request.POST['txtidd']
    ven=request.POST['txtidv']
    com=request.POST['txtcom']
    fec=request.POST['fec']
    mot=request.POST['txtmot']
    can=request.POST['numcan']
    est=request.POST['txtest']
    guardarDevo=Devolucion.objects.create(
        id_devo=dev,id_venta=ven,id_comic=com,fecha_devo=fec,motivo=mot,cantidad=can,estado=est
    )
    return redirect('Devolucion')

def selecDev(request,id):
    dev=Devolucion.objects.get(id_devo=id)
    return render(request,'editardev.html',{"ndev":dev})

def editDev(request):
    dev=request.POST['txtidd']
    ven=request.POST['txtidv']
    com=request.POST['txtcom']
    fec=request.POST['fec']
    mot=request.POST['txtmot']
    can=request.POST['numcan']
    est=request.POST['txtest']
    dev=Devolucion.objects.get(id_devo=dev)
    dev.id_venta=ven
    dev.id_comic=com
    dev.fecha_devo=fec
    dev.motivo=mot 
    dev.cantidad=can
    dev.estado=est
    dev.save()
    return redirect('Devolucion')

def borrarDev(request,id):
    dev=Devolucion.objects.get(id_devo=id)
    dev.delete()
    return redirect('Devolucion')
    