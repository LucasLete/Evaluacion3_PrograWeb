from django.shortcuts import render

from .models import Producto, Categoria


# Create your views here.


def index(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request, 'productos/index.html', context)

def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos/productos_list.html', context)

def productosAdd(request):
    if request.method is not "POST":
        categorias= Categoria.objects.all()
        context={'categorias': categorias}
        return render(request, 'productos/productos_add.html', context)
    

    else:



        id_producto=request.POST["id_producto"]
        nombre_producto=request.POST["nombre_producto"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        categoria=request.POST["categoria"]
        foto=request.POST["foto"]

        objCategoria=Categoria.objects.get(id_categoria = categoria)
        obj=Producto.objects.create(id_producto=id_producto,
                                    nombre_producto=nombre_producto,
                                    precio=precio,
                                    descripcion=descripcion,
                                    categoria=objCategoria,
                                    foto=foto )
        


        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'productos/productos_add.html', context)
    

def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)

        producto.delete()
        mensaje="Bien, datos eliminados..."
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje':mensaje}
        return render(request, 'productos/productos_list.html', context)
    except:
        mensaje="Error, id no existe..."
        productos = Producto.objects.all()
        context = {"prodcutos": productos, 'mensaje':mensaje}
        return render(request, 'productos/productos_list.html', context)

def productos_findEdit(request,pk):

    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        categorias=Categoria.objects.all()

        print(type(producto.id_categoria.categoria))

        context={'producto':producto,'categorias':categorias}
        if producto:
            return render(request, 'productos/productos_edit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'productos/productos_list.html', context)



def productosUpdate(request):
    if request.method == "POST":

        id_producto=request.POST["id_producto"]
        nombre_producto=request.POST["nombre_producto"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        categoria=request.POST["categoria"]
        foto=request.POST["foto"]

        objCategoria=Producto.objects.get(id_categoria = categoria)

        producto = Producto()
        producto.id_producto=id_producto
        producto.nombre_producto=nombre_producto
        producto.precio=precio
        producto.descripcion=descripcion
        producto.id_categoria=objCategoria
        producto.foto=foto
        producto.save()

        categorias=Categoria.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'categorias':categorias,'producto':producto}
        return render(request, 'productos/productos_edit.html', context)
    else:
        productos = Producto.objects.all()
        context={'productos':productos}
        return render(request, 'productos/productos_list.html', context)