
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
from Panel_Calculo.LDCxPF import LDCxPF


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
                user_creation_form.save()  # Guardar el usuario y obtener el objeto User
                username = user_creation_form.cleaned_data['username']
                password = user_creation_form.cleaned_data['password1']
                # Autenticar y hacer login del usuario recién creado
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('instanciar_tabla_ldc')
        except Exception as e:
            logging.exception(e)
            print(e)
            return HttpResponse('Error al agregar proyecto 3')

def instanciar_tabla_ldc(request):
    if request.method == 'GET':
        usuario = request.user
        # Construccion de diccionario
        ldcxpf = {'C': 40,
                  'CPP': 35,
                  'JAVA': 45,
                  'JAVASCRIPT': 42,
                  'JSP': 59,
                  'SQL': 10,
                  'PYTHON': 25,
                  'CSHARP': 58,
                  'NET': 60,
                  'GO': 20,
                  'PHP': 45,
                  }
        ldc = LDCxPF.objects.create(C=ldcxpf['C'], CPP=ldcxpf['CPP'], JAVA=ldcxpf['JAVA'], JAVASCRIPT=ldcxpf['JAVASCRIPT'],
                                    JSP=ldcxpf['JSP'], SQL=ldcxpf['SQL'], PYTHON=ldcxpf['PYTHON'], CSHARP=ldcxpf['CSHARP'],
                                    NET=ldcxpf['NET'], GO=ldcxpf['GO'], PHP=ldcxpf['PHP'], user=usuario)
        ldc.save()
        user = authenticate(username=usuario.username, password = usuario.password)
        login(request, user)
        return redirect('gestion_proyectos')
def exit(request):
    logout(request)
    return redirect('index')

