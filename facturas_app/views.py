from django.shortcuts import render,redirect
from .models import Factura
# Create your views here.
def index_facturas(request):
    fac=Factura.objects.all()
    return render(request,'gestfac.html',{'nfac':fac})

def regisFac(request):
    fac=request.POST['txtfac']
    ven=request.POST['numven']
    fec=request.POST['fec']
    tot=request.POST['numtot']
    mp=request.POST['txtmp']
    cli=request.POST['numcli']
    des=request.POST['numdes']
    guardarfac=Factura.objects.create(
        id_factura=fac,
        id_venta=ven,
        fecha_fac=fec,
        total=tot,
        metodo_pago=mp,
        id_cliente=cli,
        descuento=des
    )
    return redirect('Facturas')

def selecfac(request,id):
    fac=Factura.objects.get(id_factura=id)
    return render(request,'editarfac.html',{"nfac":fac})

def editfac(request):
    fac=request.POST['txtfac']
    ven=request.POST['numven']
    fec=request.POST['fec']
    tot=request.POST['numtot']
    mp=request.POST['txtmp']
    cli=request.POST['numcli']
    des=request.POST['numdes']
    fac=Factura.objects.get(id_factura=fac)
    fac.id_venta=ven
    fac.fecha_fac=fec
    fac.total=tot
    fac.metodo_pago=mp 
    fac.id_cliente=cli
    fac.descuento=des
    fac.save()
    return redirect('Facturas')

def borrarfac(request,id):
    fac=Factura.objects.get(id_factura=id)
    fac.delete()
    return redirect('Facturas')