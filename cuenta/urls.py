#from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login,LoginView
from django.contrib import admin
from django.urls import path, include
from cuenta import views
from . import views
#from project_pack import views



urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    #path('login/', views.login, name='login'),
    path('register/', views.register, name= 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.exit, name = 'exit' ),
]
