from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cambio_precios", views.cambio_precios, name="cambio_precios"),
    path("cambio_precios/<str:msj>", views.cambio_precios, name="cambio_precios"),
    path("crear_orden", views.crear_orden, name="crear_orden"),
    path("crear_orden/<str:mensaje>", views.crear_orden, name="crear_orden"),
    path("ver_orden/<str:id>", views.ver_orden, name="ver_orden"),

]