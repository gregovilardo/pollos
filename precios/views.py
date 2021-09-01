from django.shortcuts import render
from .models import User, Cliente, Producto, Orden
from django.forms import ModelForm, widgets
from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

PRODUCTOS = ["Pata Muslo", "Pechuga", "Cajon Rosario", "Cajon Glaciar",
             "Alita", "Mila de Pollo", "Pechuga Fileteada", "Pata Muslo Deshuesada"]


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "ubic"]


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["precio"]


class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = ["Pa", "Mp", "A", "Pe", "Cr", "Cg", "Hp",
                  "M", "C", "Mv", "Mc", "PeF", "PaD", "Troc", "Po"]


def index(request):
    ordenes = Orden.objects.all()

    return render(request, "precios/index.html", {"ordenes": ordenes})


def cambio_precios(request, msj=None):
    productos = Producto.objects.all()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        id = request.POST["productos"]
        if form.is_valid():
            precio = form.cleaned_data["precio"]
            producto = Producto.objects.get(pk=id)
            producto.precio = precio
            producto.save()
            return redirect(reverse("cambio_precios", kwargs={"msj": f"cambio el precio de {producto.nombre} por ${precio}"}))
        return render(request, "precios/cambio_precios.html", {"form": form, "productos": productos})
    else:
        form_producto = ProductoForm()
        return render(request, "precios/cambio_precios.html", {"form": form_producto, "productos": productos, "msj": msj})


def crear_orden(request, mensaje=None):
    clientes = Cliente.objects.all()
    if request.method == "POST":
        form = OrdenForm(request.POST)
        id = request.POST.get("clientes", False)
        if form.is_valid():
            Mp = form.cleaned_data["Mp"]
            Pa = form.cleaned_data["Pa"]
            A = form.cleaned_data["A"]
            Pe = form.cleaned_data["Pe"]
            Cr = form.cleaned_data["Cr"]
            Cg = form.cleaned_data["Cg"]
            Hp = form.cleaned_data["Hp"]
            M = form.cleaned_data["M"]
            C = form.cleaned_data["C"]
            Mv = form.cleaned_data["Mv"]
            Mc = form.cleaned_data["Mc"]
            Po = form.cleaned_data["Po"]
            PeF = form.cleaned_data["PeF"]
            PaD = form.cleaned_data["PaD"]
            Troc = form.cleaned_data["Troc"]
            total = Mp * Producto.objects.get(abrev="Mp").precio + A * Producto.objects.get(abrev="A").precio + Pe * Producto.objects.get(abrev="Pe").precio + Cr * Producto.objects.get(abrev="Cr").precio + Cg * Producto.objects.get(abrev="Cg").precio + Hp * Producto.objects.get(abrev="Hp").precio + M * Producto.objects.get(abrev="M").precio + C * Producto.objects.get(abrev="C").precio + Mv * Producto.objects.get(abrev="Mv").precio + Mc * Producto.objects.get(abrev="Mc").precio + Po * Producto.objects.get(abrev="Po").precio + PeF * Producto.objects.get(abrev="PeF").precio + PaD * Producto.objects.get(abrev="PaD").precio + Troc * Producto.objects.get(abrev="Troc").precio + Pa * Producto.objects.get(abrev="Pa").precio
            orden = Orden(cliente=Cliente.objects.get(pk=id), Po=Po, Mp=Mp, A=A, Pe=Pe, Cr=Cr, Cg=Cg, Hp=Hp, M=M, C=C, Mv=Mv, Mc=Mc, PeF=PeF, PaD=PaD, Pa=Pa, Troc=Troc, total=total)
            orden.save()
            return redirect(reverse("crear_orden", kwargs={"mensaje": f"Orden total={total}, para={Cliente.objects.get(pk=id).nombre} con Pa: {Pa} Mp: {Mp} A: {A} Pe: {Pe} Cr: {Cr} Cg: {Cg} Hp: {Hp} M: {M} C: {C} Mv: {Mv} Mc: {Mc} PeF: {PeF} PaD: {PaD} Troc: {Troc}"}))
        else:
            return render(request, "precios/crear_orden.html", {"form": form, "clientes": clientes, "mensaje": "ERROR"})

    else:
        form = OrdenForm()
        return render(request, "precios/crear_orden.html", {"form": form, "clientes": clientes, "mensaje": mensaje})


def ver_orden(request, id):
    orden = Orden.objects.get(pk=id)
    if request.method == "POST":
        
        if request.POST.getlist("entregado"):
            orden.entregado = True
            orden.save()
        if request.POST.getlist("cobrado"):
            orden.cobrado = True
            orden.save()
        return redirect(reverse("index"))
    else:
        return render(request, "precios/ver_orden.html", {"orden":orden})