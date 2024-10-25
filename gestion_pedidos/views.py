from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from gestion_pedidos.models import Articulo
from django.conf import settings

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

        # Enviar email:
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["machucagelvez@outlook.es"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return render(request, "contacto.html")
