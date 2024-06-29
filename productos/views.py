from django.shortcuts import render, get_object_or_404

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

from django.shortcuts import render
from .models import Producto, Categoria

def productosAdd(request):
    if request.method != "POST":
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'productos/productos_add.html', context)
    else:
        id_producto = request.POST["ID_Producto"]
        nombre_producto = request.POST["Nombre_Producto"]
        precio = request.POST["Precio"]
        descripcion = request.POST["Descripcion"]
        categoria = request.POST["Categoria"]
        foto = request.FILES["Foto"]

        objCategoria = Categoria.objects.get(id_categoria=categoria)
        obj = Producto.objects.create(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio=precio,
            descripcion=descripcion,
            id_categoria=objCategoria,
            foto=foto
        )

        obj.save()
        context = {'mensaje': "Ok, datos grabados..."}
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

        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripcion"]
        categoria_id = request.POST["categoria"]
        foto = request.POST["foto"]

        # Obtener la instancia de Producto que deseas actualizar
        producto = get_object_or_404(Producto, id_producto=id_producto)

        # Obtener la instancia de Categoria correcta
        objCategoria = get_object_or_404(Categoria, id_categoria=categoria_id)

        # Actualizar los campos del producto
        producto.nombre_producto = nombre_producto
        producto.precio = precio
        producto.descripcion = descripcion
        producto.id_categoria = objCategoria  # Asegúrate de asignar la instancia de Categoria
        producto.foto = foto

        producto.save()

        # Obtener todas las categorías para el contexto
        categorias = Categoria.objects.all()
        context = {'mensaje': "Ok, datos actualizados...", 'categorias': categorias, 'producto': producto}
        return render(request, 'productos/productos_edit.html', context)
    else:
        # Si no es una solicitud POST, simplemente mostrar la lista de productos
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'productos/productos_list.html', context)


def inicio(request):
    return render(request, 'productos/inicio.html')

def login(request):
    return render(request, 'productos/login.html')

def jardineria(request):
    return render(request, 'productos/jardineria.html')

def Registrarse(request):
    return render(request, 'productos/Registrarse.html')