from django.urls import path
from api_app import views

urlpatterns = [
    path('pasajeros/', views.pasajero_list),
    path('pasajeros/<int:pk>', views.pasajero_detail),
    path('trayectos/', views.trayecto_list),
    path('trayectos/<int:pk>', views.trayecto_detail),
    path('choferes/', views.chofer_list),
    path('choferes/<int:pk>', views.chofer_detail),
    path('buses/promedios', views.listar_promedio_pasajeros),
    path('trayectos/<int:pk>/capacidad/<int:porcentaje>', views.filtrar_porcentaje_pasajeros_por_trayecto),	
    # path('choferes/<int:pk>', views.chofer_detail),
    # path('choferes/<int:pk>/promedio', views.listar_promedio_pasajeros),
    path('buses/', views.bus_list),
    path('buses/<int:pk>', views.bus_detail),
]