from django.contrib import admin
from Panel_Calculo.PuntosFuncion import PuntosFuncion
from Panel_Calculo.KLDC import KLDC
from Panel_Calculo.LDCxPF import LDCxPF
from Panel_Calculo.Planeacion import Planeacion
from Panel_Calculo.Esfuerzo import Esfuerzo
# Register your models here.
admin.site.register(PuntosFuncion)
admin.site.register(KLDC)
admin.site.register(LDCxPF)
admin.site.register(Planeacion)
admin.site.register(Esfuerzo)