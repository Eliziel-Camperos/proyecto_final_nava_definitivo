from django.shortcuts import render,redirect
from .models import Comics
 
# Create your views here.
def index_Comic(request):
    nComics=Comics.objects.all()
    return render(request,'gestComic.html',{'mComics':nComics})

def regisComics(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    cate=request.POST["txtcate"]
    autor=request.POST["txtaut"]
    serie=request.POST["txtser"]
    precio=request.POST["numpre"]
    
    guarComics=Comics.objects.create(
            id_comics=id,nombre=nombre,categoria=cate,autor=autor,serie=serie,precio=precio
    )
    return redirect("Comics")

def selecCom(request,id):
    com=Comics.objects.get(id_comics=id)
    return render(request,'editarComic.html',{"mComics":com})

def editCom(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    cate=request.POST["txtcate"]
    autor=request.POST["txtaut"]
    serie=request.POST["txtser"]
    precio=request.POST["numpre"]
    com=Comics.objects.get(id_comics=id)
    com.nombre=nombre
    com.categoria=cate
    com.autor=autor
    com.serie=serie
    com.precio=precio   
    com.save()
    return redirect('Comics')

def borrarCom(request,id):
    com=Comics.objects.get(id_comics=id)
    com.delete()
    return redirect('Comics')