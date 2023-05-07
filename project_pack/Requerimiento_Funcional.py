from django.db import models
from project_pack.Macrofuncionalidad import Macrofuncionalidad

class Requerimiento_Funcional(models.Model):
    requerimiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=900)
    macrofuncionalidad = models.ForeignKey(Macrofuncionalidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.requerimiento