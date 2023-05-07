from django.db import models
from project_pack.proyecto import Proyecto


class AspectosANDComplejidad(models.Model):

    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    #Entradas
    numEntradasBaja = models.SmallIntegerField()
    numEntradasMedia = models.SmallIntegerField()
    numEntradasAlta = models.SmallIntegerField()
    #Salidas
    numSalidasBaja = models.SmallIntegerField()
    numSalidasMedia = models.SmallIntegerField()
    numSalidasAlta = models.SmallIntegerField()
    #Consultas
    numConsultasBaja = models.SmallIntegerField()
    numConsultasMedia = models.SmallIntegerField()
    numConsultasAlta = models.SmallIntegerField()
    #Archivos Internos
    numArchivosInternosBaja = models.SmallIntegerField()
    numArchivosInternosMedia = models.SmallIntegerField()
    numArchivosInternosAlta = models.SmallIntegerField()
    #Archivos Externos
    numExternosBaja = models.SmallIntegerField()
    numExternosMedia = models.SmallIntegerField()
    numExternosAlta = models.SmallIntegerField()

    def __str__(self):
        return f"{self.proyecto.nombre} - Entradas (Baja: {self.numEntradasBaja}, Media: {self.numEntradasMedia}, Alta: {self.numEntradasAlta}) - Salidas (Baja: {self.numSalidasBaja}, Media: {self.numSalidasMedia}, Alta: {self.numSalidasAlta}) - Consultas (Baja: {self.numConsultasBaja}, Media: {self.numConsultasMedia}, Alta: {self.numConsultasAlta}) - Archivos Internos (Baja: {self.numArchivosInternosBaja}, Media: {self.numArchivosInternosMedia}, Alta: {self.numArchivosInternosAlta}) - Archivos Externos (Baja: {self.numExternosBaja}, Media: {self.numExternosMedia}, Alta: {self.numExternosAlta})"


