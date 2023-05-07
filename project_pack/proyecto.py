from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=500)
    tipo_proyecto = models.CharField(max_length=50)
    lenguaje = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre