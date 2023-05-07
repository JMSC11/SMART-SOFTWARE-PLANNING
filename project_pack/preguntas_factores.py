from django.db import models
from project_pack.proyecto import Proyecto

class preguntas_factores(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    p1 = models.CharField(max_length=1500)
    p2 = models.CharField(max_length=1500)
    p3 = models.CharField(max_length=1500)
    p4 = models.CharField(max_length=1500)
    p5 = models.CharField(max_length=1500)
    p6 = models.CharField(max_length=1500)
    p7 = models.CharField(max_length=1500)
    p8 = models.CharField(max_length=1500)
    p9 = models.CharField(max_length=1500)
    p10 = models.CharField(max_length=1500)
    p11 = models.CharField(max_length=1500)
    p12 = models.CharField(max_length=1500)
    p13 = models.CharField(max_length=1500)
    p14 = models.CharField(max_length=1500)

    def __str__(self):
        return self.p1
