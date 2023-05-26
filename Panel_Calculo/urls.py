#from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login,LoginView
from django.urls import path
from . import views



urlpatterns = [

    path('Panel_Calculo/', views.Panel_Calculo, name='Panel_Calculo'),
    path('Eleccion_Proyecto/', views.Eleccion_Proyecto, name='Eleccion_Proyecto'),
    path('Puntos_Funcion/<id>', views.Puntos_Funcion, name='Puntos_Funcion'),
    path('KLDC_VIEW/<id>', views.KLDC_VIEW, name='KLDC_VIEW'),
    path('Planeacion/<id>', views.getPlaneacion, name='Planeacion'),
    path('Esfuerzo/<id>', views.getEsfuerzo, name='Esfuerzo'),
    path('editar_tabla_pf_ldc/<id>', views.editar_tabla_pf_ldc, name='editar_tabla_pf_ldc'),


]
