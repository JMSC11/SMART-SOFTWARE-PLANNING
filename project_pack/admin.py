from django.contrib import admin

from project_pack.preguntas_factores import preguntas_factores
from project_pack.proyecto import Proyecto
from project_pack.AspectosANDComplejidad import AspectosANDComplejidad
from project_pack.Multiplicador_Influencia import Multiplicador_Influencia
from project_pack.Requerimiento_Funcional import Requerimiento_Funcional
from project_pack.Requerimiento_no_Funcional import Requerimiento_no_Funcional
from Panel_Calculo.PuntosFuncion import PuntosFuncion
# Register your models here.
admin.site.register(Proyecto)
admin.site.register(AspectosANDComplejidad)
admin.site.register(Multiplicador_Influencia)
admin.site.register(Requerimiento_Funcional)
admin.site.register(Requerimiento_no_Funcional)
admin.site.register(preguntas_factores)
admin.site.register(PuntosFuncion)
