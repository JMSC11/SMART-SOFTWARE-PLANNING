#from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login,LoginView
from django.urls import path
from . import views



urlpatterns = [

    path('Panel_Calculo/', views.Panel_Calculo, name='Panel_Calculo'),
    path('Eleccion_Proyecto/', views.Eleccion_Proyecto, name='Eleccion_Proyecto'),

]
