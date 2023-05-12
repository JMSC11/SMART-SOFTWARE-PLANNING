from django.db import models
from project_pack.proyecto import Proyecto

# Create your models here.
class KLDC(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    KLDC = models.FloatField()



