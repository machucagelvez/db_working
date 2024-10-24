from django.http import HttpResponse
from django.shortcuts import render

from gestion_pedidos.models import Articulo

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["prd"]:
        # mensaje = "Artículo buscado: %r" % request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto) > 20:
            mensaje = "Texto demasiado extenso"
        else:
            # articulos = Articulo.objects.filter(nombre=producto)
            # nombre__icontains = like en sql:
            articulos = Articulo.objects.filter(nombre__icontains=producto)

            return render(
                request,
                "resultados_busqueda.html",
                {"articulos": articulos, "query": producto},
            )
    else:
        mensaje = "Debes escribir algo para buscar"

    return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")
