from django.contrib import admin
from .models import User, Cliente, Producto, Orden
# Register your models here.

admin.site.register(User)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Orden)