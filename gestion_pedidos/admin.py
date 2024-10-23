from django.contrib import admin
from gestion_pedidos.models import Articulo, Cliente, Pedido

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    # Permite definir los campos que se ven en el panel de administración:
    list_display = ("nombre", "direccion", "email", "telefono")

    # Permite definir los campos que se pueden buscar:
    search_fields = ("nombre", "direccion")


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion")
    # Permite filtrar los artículos por sección:
    list_filter = ("seccion",)  # La coma se agrega para indicar que es una tupla.


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidosAdmin)
