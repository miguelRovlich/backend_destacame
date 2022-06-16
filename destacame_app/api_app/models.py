from django import db
from django.db import models
# Create your models here.

class Chofer(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Choferes"
        db_table = 'api_app_choferes'

class Trayecto(models.Model):
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Trayectos"
        db_table = 'api_app_trayectos'

class Bus(models.Model):
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    # capacidad = models.IntegerField()
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    horario_salida = models.TimeField(null=True)
    horario_llegada = models.TimeField(null=True)
    class Meta:
        verbose_name_plural = "Buses"
        db_table = 'api_app_buses'
class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,null=True)
    asiento = models.IntegerField(unique=True,null=True)
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.bus) + " " + str(self.asiento)
    class Meta:
        verbose_name_plural = "Pasajeros"
        db_table = 'api_app_pasajeros'
