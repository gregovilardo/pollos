from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import CharField

# Create your models here.

def min_value(value):
    if value < 0.0:
        raise ValidationError(_("El precio debe ser positivo"), params={"value": value},)


class User(AbstractUser):
    pass


class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    ubic = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombre} {self.ubic}"

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    abrev = models.CharField(max_length=20)
    precio = models.FloatField(validators=[min_value])

    def __str__(self):
        return f"{self.nombre} {self.abrev} {self.precio}"


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Mp = models.FloatField(validators=[min_value], default=0)
    Pa = models.FloatField(validators=[min_value], default=0)
    A = models.FloatField(validators=[min_value], default=0)
    Pe = models.FloatField(validators=[min_value], default=0)
    Cr = models.FloatField(validators=[min_value], default=0)
    Cg = models.FloatField(validators=[min_value], default=0)
    Hp = models.FloatField(validators=[min_value], default=0)
    M = models.FloatField(validators=[min_value], default=0)
    C = models.FloatField(validators=[min_value], default=0)
    Mv = models.FloatField(validators=[min_value], default=0)
    Mc = models.FloatField(validators=[min_value], default=0)
    PeF = models.FloatField(validators=[min_value], default=0)
    Po = models.FloatField(validators=[min_value], default=0)
    PaD = models.FloatField(validators=[min_value], default=0)
    Troc = models.FloatField(validators=[min_value], default=0)
    cobrado = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)
    total = models.FloatField(validators=[min_value], default=0)

    def __str__(self):
        return f"{self.cliente} {self.total} {self.cobrado} {self.entregado}"