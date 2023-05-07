from django.db import models
from project_pack.proyecto import Proyecto

class Requerimiento_no_Funcional(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    requerimiento = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=1500)

    def __str__(self):
        return self.requerimiento