from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.
def index_Venta(request):
    nVenta=Venta.objects.all()
    return render(request,'gestVen.html',{'mVenta':nVenta})

def regisVenta(request): 
    idt=request.POST["txtidt"]
    idc=request.POST["txtidc"]
    ide=request.POST["txtide"]
    fec=request.POST["fec"]
    cant=request.POST["numcan"]
    total=request.POST["numtot"]
    
    
    guarVenta=Venta.objects.create(
            id_tienda=idt,id_comic=idc,id_empleado=ide,fecha_venta=fec,Cant_comic=cant,total=total
    )
    return redirect("Venta")

def selecVen(request,id):
    ven=Venta.objects.get(id_tienda=id)
    return render(request,'editarVen.html',{"mVenta":ven})

def editVen(request):
    idt=request.POST["txtidt"]
    idc=request.POST["txtidc"]
    ide=request.POST["txtide"]
    fec=request.POST["fec"]
    cant=request.POST["numcan"]
    total=request.POST["numtot"]
    ven=Venta.objects.get(id_tienda=idt)
    ven.id_comic=idc
    ven.id_empleado=ide
    ven.fecha_venta=fec
    ven.Cant_comic=cant 
    ven.total=total
    ven.save()
    return redirect('Venta')

def borrarVen(request,id):
    Ven=Venta.objects.get(id_tienda=id)
    Ven.delete()
    return redirect('Venta')