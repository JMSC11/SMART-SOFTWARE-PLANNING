from django.db import models
from project_pack.proyecto import Proyecto

class Macrofuncionalidad(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    macrofuncionalidad = models.CharField(max_length=255)
    usuarios = models.CharField(max_length=255)

    def __str__(self):
        return self.macrofuncionalidad