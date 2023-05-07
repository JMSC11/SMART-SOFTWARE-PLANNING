from http.client import HTTPResponse

import django.http
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm
from .Cuenta import Cuenta
from .forms import RegistroCuenta


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'registration/register.html', data)
    else:
        try:
            user_creation_form = CustomUserCreationForm(data=request.POST)
            if user_creation_form.is_valid():
                user_creation_form.save()
                #user = authenticate(username=user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
                #login(request, user)
                return redirect('index')
        except Exception as e:

            logging.exception(e)
            print(e)

            return HttpResponse('Error al agregar proyecto 3')

def exit(request):
    logout(request)
    return redirect('index')

