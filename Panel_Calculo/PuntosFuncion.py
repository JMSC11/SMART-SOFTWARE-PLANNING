from django.db import models
from project_pack.proyecto import Proyecto

# Create your models here.
class PuntosFuncion(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    puntos_funcion_sin_ajustar = models.SmallIntegerField()
    puntos_funcion_ajustados = models.SmallIntegerField()
    multiplicador = models.SmallIntegerField()


