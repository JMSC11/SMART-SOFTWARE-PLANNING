import ast

from django.contrib.auth.decorators import login_required
import logging
from django.db import transaction
from django.shortcuts import render, get_object_or_404

from project_pack.preguntas_factores import preguntas_factores
from project_pack.proyecto import Proyecto
from project_pack.AspectosANDComplejidad import AspectosANDComplejidad
from project_pack.Multiplicador_Influencia import Multiplicador_Influencia
from Panel_Calculo.PuntosFuncion import PuntosFuncion
from Panel_Calculo.KLDC import KLDC
from project_pack.Requerimiento_Funcional import Requerimiento_Funcional
from project_pack.Requerimiento_no_Funcional import Requerimiento_no_Funcional
from project_pack.Macrofuncionalidad import Macrofuncionalidad
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
@login_required()
def Panel_Calculo(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        return render(request, 'Panel_Calculo.html', {'proyecto': proyecto})


@login_required()
def Eleccion_Proyecto(request):
    if request.method == 'GET':
        user_id = request.user.id
        proyectos = Proyecto.objects.filter(user = user_id)
        return render(request, 'Eleccion_Proyecto.html', {'proyectos': proyectos})
        #return render(request, 'gestion_proyectos.html')
    else:
        print(request.POST)
        id_proyecto = request.POST['id_proyecto']
        name = request.POST['name']
        request.session['id_proyecto'] = id_proyecto
        print(name)
        print(id_proyecto)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        # lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        # lista_requerimientos = []
        # for macro in lista_macrofuncionalidad:
        #     lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))
        # print(lista_requerimientos)
        # lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
        # print(lista_no_funcionales)
        # aspectos = AspectosANDComplejidad.objects.filter(proyecto=proyecto)
        # print(aspectos)
        # return render(request, 'Panel_Calculo.html', {'proyecto': proyecto,
        #                                                   'lista_macrofuncionalidad': lista_macrofuncionalidad,
        #                                                   'lista_requerimientos_funcionales' : lista_requerimientos,
        #                                                   'lista_no_funcionales': lista_no_funcionales,
        #                                                   'aspectos' : aspectos,
        #                                                   })
        return render(request, 'Panel_Calculo.html', {'proyecto' : proyecto})


def Puntos_Funcion(request, id):
    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=id)
        aspectos = get_object_or_404(AspectosANDComplejidad, pk=id)
        preguntas = preguntas_factores.objects.get(proyecto=proyecto)
        multiplicador = Multiplicador_Influencia.objects.get(proyecto=proyecto)

        operaciones = { 'm1' : aspectos.numEntradasBaja * 3,
                        'm2' : aspectos.numEntradasMedia *4,
                        'm3' : aspectos.numEntradasAlta *6,
                        'm4' : aspectos.numSalidasBaja *4,
                        'm5' : aspectos.numSalidasMedia *5,
                        'm6' : aspectos.numSalidasAlta *7,
                        'm7' : aspectos.numConsultasBaja *3,
                        'm8' : aspectos.numConsultasMedia *4,
                        'm9' : aspectos.numConsultasAlta *6,
                        'm10' : aspectos.numArchivosInternosBaja *7,
                        'm11' : aspectos.numArchivosInternosMedia *10,
                        'm12' : aspectos.numArchivosInternosAlta *15,
                        'm13' : aspectos.numExternosBaja *5,
                        'm14' : aspectos.numExternosMedia *7,
                        'm15' : aspectos.numExternosAlta *10,
                        }
        subtotal_baja = operaciones["m1"] + operaciones["m4"] + operaciones["m7"] + operaciones["m10"] + operaciones["m13"]
        subtotal_media = operaciones["m2"] + operaciones["m5"] + operaciones["m8"] + operaciones["m11"] + operaciones["m14"]
        subtotal_alta = operaciones["m3"] + operaciones["m6"] + operaciones["m9"] + operaciones["m12"] + operaciones["m15"]
        total = subtotal_baja + subtotal_media + subtotal_alta
        val_ajus_compl = multiplicador.Answer1 + multiplicador.Answer2 + multiplicador.Answer3 + multiplicador.Answer4 + multiplicador.Answer5 + multiplicador.Answer6
        val_ajus_compl += multiplicador.Answer7 + multiplicador.Answer8 + multiplicador.Answer9 + multiplicador.Answer10 + multiplicador.Answer11 + multiplicador.Answer12
        val_ajus_compl += multiplicador.Answer13 + multiplicador.Answer14

        fac_multi = 0.01 * val_ajus_compl
        sum = 0.65 + fac_multi
        PFA = total * sum
        # if not ModeloSecundario.objects.filter(modelo_principal_id=modelo_principal_id).exists():
        #     # No existe un registro con la misma clave foránea
        #     # Puedes realizar otras validaciones o procesamientos antes de guardar el objeto
        #     modelo_secundario = ModeloSecundario(modelo_principal_id=modelo_principal_id)
        #     modelo_secundario.save()
        if not PuntosFuncion.objects.filter(proyecto_id = id):
            PuntosFuncionAjustados = PuntosFuncion.objects.create(puntos_funcion_sin_ajustar = total, puntos_funcion_ajustados = PFA, multiplicador = val_ajus_compl, proyecto=proyecto )
            PuntosFuncionAjustados.save()

        return render(request, 'puntos_funcion.html', {'proyecto' : proyecto,
                                                       'aspectos': aspectos,
                                                       'operaciones': operaciones,
                                                       'subtotal_baja' : subtotal_baja,
                                                       'subtotal_media' : subtotal_media,
                                                       'subtotal_alta' : subtotal_alta,
                                                       'total' : total,
                                                       'preguntas': preguntas,
                                                       'respuestas' : multiplicador,
                                                       'val_ajus_compl' : val_ajus_compl,
                                                       'fac_multi' : fac_multi,
                                                        'PFA' : PFA,
                                                       'sum' : sum,
                                                       })

def KLDC_VIEW(request, id):
    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=id)
        PFA = PuntosFuncion.objects.get(proyecto = proyecto)
        #Construccion de diccionario
        LDCxPF = {'C' : 28,
                  'C++' : 24,
                  'Java' : 45,
                  'JavaScript' : 37,
                  'JSP' : 54,
                  'SQL' : 5,
                  'Python' : 15,
                  'C#' : 53,
                  '.NET' : 55,
                  'GO' : 20,
                  }
        value = LDCxPF[proyecto.lenguaje]
        LDC = PFA.puntos_funcion_ajustados * value
        v_KLDC = LDC/1000
        if not KLDC.objects.filter(proyecto_id = id):
            kldc = KLDC.objects.create( KLDC = v_KLDC, proyecto=proyecto )
            kldc.save()
        return render(request, 'kldc.html', {'proyecto' : proyecto,
                                             'PFA' : PFA,
                                             'KLDC' : v_KLDC,
                                             'LDCxPF' : LDCxPF,
                                             'value' : value,
                                             'LDC' : LDC,
                                             })