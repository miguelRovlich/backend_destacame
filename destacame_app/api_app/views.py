from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api_app.models import Pasajero, Chofer, Trayecto, Bus
from api_app.serializers import PasajeroSerializer, ChoferSerializer, TrayectoSerializer, BusSerializer
# Create your views here.

#list all pasajeros
@csrf_exempt
def pasajero_list(request):
    if request.method == 'GET':
        pasajeros = Pasajero.objects.all()
        #serialize data
        pasajero_serializer = PasajeroSerializer(pasajeros, many=True)
        return JsonResponse(pasajero_serializer.data, safe=False)
    elif request.method == 'POST':
        pasajero_data = JSONParser().parse(request)
        pasajero_serializer = PasajeroSerializer(data=pasajero_data)
        if pasajero_serializer.is_valid():
            pasajero_serializer.save()
            return JsonResponse(pasajero_serializer.data, status=201)
        return JsonResponse(pasajero_serializer.errors, status=400)
#add pasajero to db
@csrf_exempt
def pasajero_detail(request, pk):
    try:
        pasajero = Pasajero.objects.get(pk=pk)
    except Pasajero.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        pasajero_serializer = PasajeroSerializer(pasajero)
        return JsonResponse(pasajero_serializer.data)
    elif request.method == 'PUT':
        pasajero_data = JSONParser().parse(request)
        pasajero_serializer = PasajeroSerializer(pasajero, data=pasajero_data)
        if pasajero_serializer.is_valid():
            pasajero_serializer.save()
            return JsonResponse(pasajero_serializer.data)
        return JsonResponse(pasajero_serializer.errors, status=400)
    elif request.method == 'DELETE':
        pasajero = Pasajero.objects.get(pk=pk)
        pasajero.delete()
        return HttpResponse(status=204)
#create crud for Trayecto
@csrf_exempt
def trayecto_list(request):
    if request.method == 'GET':
        trayectos = Trayecto.objects.all()
        #serialize data
        trayecto_serializer = TrayectoSerializer(trayectos, many=True)
        return JsonResponse(trayecto_serializer.data, safe=False)
    elif request.method == 'POST':
        trayecto_data = JSONParser().parse(request)
        trayecto_serializer = TrayectoSerializer(data=trayecto_data)
        if trayecto_serializer.is_valid():
            trayecto_serializer.save()
            return JsonResponse(trayecto_serializer.data, status=201)
        return JsonResponse(trayecto_serializer.errors, status=400)
@csrf_exempt
def trayecto_detail(request,pk):
    if request.method == 'GET':
        try:
            trayecto = Trayecto.objects.get(pk=pk)
        except Trayecto.DoesNotExist:
            return HttpResponse(status=404)
        trayecto_serializer = TrayectoSerializer(trayecto)
        return JsonResponse(trayecto_serializer.data)
    elif request.method == 'PUT':
        trayecto = Trayecto.objects.get(pk=pk)
        trayecto_data = JSONParser().parse(request)
        trayecto_serializer = TrayectoSerializer(trayecto, data=trayecto_data)
        if trayecto_serializer.is_valid():
            trayecto_serializer.save()
            return JsonResponse(trayecto_serializer.data)
        return JsonResponse(trayecto_serializer.errors, status=400)
    elif request.method == 'DELETE':
        trayecto = Trayecto.objects.get(pk=pk)
        trayecto.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def chofer_list(request):
    if request.method == 'GET':
        choferes = Chofer.objects.all()
        #serialize data
        chofer_serializer = ChoferSerializer(choferes, many=True)
        return JsonResponse(chofer_serializer.data, safe=False)
    elif request.method == 'POST':
        chofer_data = JSONParser().parse(request)
        chofer_serializer = ChoferSerializer(data=chofer_data)
        if chofer_serializer.is_valid():
            chofer_serializer.save()
            return JsonResponse(chofer_serializer.data, status=201)
        return JsonResponse(chofer_serializer.errors, status=400)
@csrf_exempt
def chofer_detail(request,pk):
    if request.method == 'GET':
        try:
            chofer = Chofer.objects.get(pk=pk)
        except Chofer.DoesNotExist:
            return HttpResponse(status=404)
        chofer_serializer = ChoferSerializer(chofer)
        return JsonResponse(chofer_serializer.data)
    elif request.method == 'PUT':
        chofer = Chofer.objects.get(pk=pk)
        chofer_data = JSONParser().parse(request)
        chofer_serializer = ChoferSerializer(chofer, data=chofer_data)
        if chofer_serializer.is_valid():
            chofer_serializer.save()
            return JsonResponse(chofer_serializer.data)
        return JsonResponse(chofer_serializer.errors, status=400)
    elif request.method == 'DELETE':
        chofer = Chofer.objects.get(pk=pk)
        chofer.delete()
        return HttpResponse(status=204)

@csrf_exempt
def listar_promedio_pasajeros(request):
    if request.method == 'GET':
        trayectos = Trayecto.objects.all()
        buses_promedio = []
        for trayecto in trayectos:
            buses = Bus.objects.filter(trayecto=trayecto.id)
            for bus in buses:
                pasajeros = Pasajero.objects.filter(bus=bus.id).count()
                contador = len(buses)
                promedio = pasajeros/contador
                buses_diccionario = {
                    'id': bus.id,
                    'chofer': bus.chofer.nombre + ' ' + bus.chofer.apellido,
                    'trayecto': bus.trayecto.origen + '-' + bus.trayecto.destino,
                    'horario_salida': bus.horario_salida,
                    'horario_llegada': bus.horario_llegada,
                    'promedio_pasajeros': promedio
                }
                buses_promedio.append(buses_diccionario)
        #transformar el array en un diccionario
        buses_promedio_diccionario = {'buses': buses_promedio}
        return JsonResponse(buses_promedio_diccionario, safe=False)
@csrf_exempt
def filtrar_porcentaje_pasajeros_por_trayecto(request, pk, porcentaje):
    if request.method == 'GET':
        trayecto = Trayecto.objects.get(pk=pk)
        buses = Bus.objects.filter(trayecto=trayecto.id)
        busesValidos = []
        for bus in buses:
            pasajeros = Pasajero.objects.filter(bus=bus.id).count()
            print(pasajeros)
            porcentaje_capacidad_vendida = int(pasajeros/10*100)
            print(porcentaje_capacidad_vendida)       
            if porcentaje_capacidad_vendida >= porcentaje:
                #transformar clase bus en diccionario
                bus_dict = {
                    'id': bus.id,
                    'chofer': bus.chofer.nombre + ' ' + bus.chofer.apellido,
                    'trayecto': bus.trayecto.origen + '-' + bus.trayecto.destino,
                    'horario_salida': bus.horario_salida,
                    'horario_llegada': bus.horario_llegada,
                }
                busesValidos.append(bus_dict)
        #transformar el array en un diccionario
        busesValidos_diccionario = {'buses': busesValidos}
        return JsonResponse(busesValidos_diccionario, safe=False)

#create crud for Bus
@csrf_exempt
def bus_list(request):
    if request.method == 'GET':
        buses = Bus.objects.all()
        #serialize data
        bus_serializer = BusSerializer(buses, many=True)
        return JsonResponse(bus_serializer.data, safe=False)
    elif request.method == 'POST':
        bus_data = JSONParser().parse(request)
        bus_serializer = BusSerializer(data=bus_data)
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse(bus_serializer.data, status=201)
        return JsonResponse(bus_serializer.errors, status=400)
@csrf_exempt
def bus_detail(request,pk):
    if request.method == 'GET':
        try:
            bus = Bus.objects.get(pk=pk)
        except Bus.DoesNotExist:
            return HttpResponse(status=404)
        bus_serializer = BusSerializer(bus)
        return JsonResponse(bus_serializer.data)
    elif request.method == 'PUT':
        bus_data = JSONParser().parse(request)
        print(bus_data)
        bus = Bus.objects.get(pk=pk)
        bus_serializer = BusSerializer(bus, data=bus_data)
        print(bus_serializer.is_valid())
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse(bus_serializer.data)
        return JsonResponse(bus_serializer.errors, status=400)
    elif request.method == 'DELETE':
        bus = Bus.objects.get(pk=pk)
        bus.delete()
        return HttpResponse(status=204)