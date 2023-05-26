from django.db import models
from project_pack.proyecto import Proyecto

# Create your models here.
class Esfuerzo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    Esfuerzo_jones = models.FloatField()
    Esfuerzo_COCOMO = models.FloatField()