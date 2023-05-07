from django.db import models
from project_pack.proyecto import Proyecto

class Multiplicador_Influencia(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    Answer1 = models.SmallIntegerField()
    Answer2 = models.SmallIntegerField()
    Answer3 = models.SmallIntegerField()
    Answer4 = models.SmallIntegerField()
    Answer5 = models.SmallIntegerField()
    Answer6 = models.SmallIntegerField()
    Answer7 = models.SmallIntegerField()
    Answer8 = models.SmallIntegerField()
    Answer9 = models.SmallIntegerField()
    Answer10 = models.SmallIntegerField()
    Answer11 = models.SmallIntegerField()
    Answer12 = models.SmallIntegerField()
    Answer13 = models.SmallIntegerField()
    Answer14 = models.SmallIntegerField()

   # multiplicador = models.DecimalField(max_digits=2, decimal_places=2)


def __str__(self):
    return str(self.Answer1)