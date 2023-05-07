from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass
class RegistroCuenta(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=50)
    usuario = forms.CharField(label="usuario", max_length=50)
    email = forms.CharField(label="email", max_length=20)
    password = forms.CharField(label="password", max_length=20)