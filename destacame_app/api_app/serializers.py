#create serializers from models
from rest_framework import serializers
from api_app.models import Pasajero, Chofer, Trayecto, Bus
#
class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ('id', 'nombre', 'apellido', 'bus', 'asiento')
class ChoferSerializer(serializers.ModelSerializer):
   class Meta:
       model = Chofer
       fields = ('id', 'nombre', 'apellido')
class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = ('id', 'origen', 'destino')
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id','chofer', 'trayecto', 'horario_salida', 'horario_llegada')
