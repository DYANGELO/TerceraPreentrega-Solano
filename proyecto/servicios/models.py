from django.db import models

# Create your models here.

class Juegos(models.Model):
    juego = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.juego} - ${self.precio}"

class Sorteos(models.Model):
    Sorteo = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.Sorteo}"

class Promociones(models.Model):
    promocion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.promocion}"