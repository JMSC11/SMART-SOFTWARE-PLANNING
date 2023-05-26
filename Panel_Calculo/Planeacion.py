from django.db import models
from project_pack.proyecto import Proyecto

# Create your models here.
class Planeacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    Planeacion_jones = models.FloatField()
    Planeacion_COCOMO = models.FloatField()



