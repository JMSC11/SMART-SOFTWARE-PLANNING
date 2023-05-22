from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from project_pack.preguntas_factores import preguntas_factores
from project_pack.proyecto import Proyecto
from project_pack.AspectosANDComplejidad import AspectosANDComplejidad
from project_pack.Multiplicador_Influencia import Multiplicador_Influencia
from Panel_Calculo.PuntosFuncion import PuntosFuncion
from Panel_Calculo.KLDC import KLDC
from Panel_Calculo.LDCxPF import LDCxPF
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
    else:
        print(request.POST)
        id_proyecto = request.POST['id_proyecto']
        name = request.POST['name']
        request.session['id_proyecto'] = id_proyecto
        print(name)
        print(id_proyecto)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        return render(request, 'Panel_Calculo.html', {'proyecto' : proyecto})

def Calcular_Metricas(id):
    puntos_funcion  = Calcular_PF(id)

    return puntos_funcion
    #Aquí se deben de guardar los resultados. si es que ya existe, entonces actualizar


def Puntos_Funcion(request, id):
    if request.method == 'GET':
        puntos_de_funcion = Calcular_PF(id)
        return render(request, 'puntos_funcion.html', {'puntos_de_funcion' : puntos_de_funcion})
def KLDC_VIEW(request, id):
    usuario = request.user
    if request.method == 'GET':
        tabla_ldc = LDCxPF.objects.get(user=usuario)
        lineas_codigo = Calcular_KLDC(id, usuario)
        atributos_valores = vars(tabla_ldc)
        atributos_valores = {key: value for key, value in atributos_valores.items() if key not in ['id', '_state', 'user_id']}
        return render(request, 'kldc.html', {'lineas_codigo' : lineas_codigo,
                                             'atributos_valores' : atributos_valores,
                                             'usuario' : usuario,
                                             })
    else:
        tabla_ldc = LDCxPF.objects.get(user=usuario)
        tabla_ldc.C = request.POST['C']
        tabla_ldc.CPP = request.POST['CPP']
        tabla_ldc.JAVA = request.POST['JAVA']
        tabla_ldc.JAVASCRIPT = request.POST['JAVASCRIPT']
        tabla_ldc.JSP = request.POST['JSP']
        tabla_ldc.SQL = request.POST['SQL']
        tabla_ldc.PYTHON = request.POST['PYTHON']
        tabla_ldc.CSHARP = request.POST['CSHARP']
        tabla_ldc.NET = request.POST['NET']
        tabla_ldc.GO = request.POST['GO']
        tabla_ldc.PHP = request.POST['PHP']
        tabla_ldc.save()
        return redirect('KLDC_VIEW', id)

def Calcular_KLDC(id, usuario):
    proyecto = get_object_or_404(Proyecto, pk=id)
    PFA = PuntosFuncion.objects.get(proyecto=proyecto)
    tabla_ldc = LDCxPF.objects.get(user=usuario)
    # Construccion de diccionario
    nombre_atributo = proyecto.lenguaje  # El nombre del atributo que deseas buscar

    value = getattr(tabla_ldc, nombre_atributo)
    LDC = PFA.puntos_funcion_ajustados * value
    v_KLDC = LDC / 1000
    if not KLDC.objects.filter(proyecto_id=id):
        kldc = KLDC.objects.create(KLDC=v_KLDC, proyecto=proyecto)
        kldc.save()
    else:
        kldc=KLDC.objects.get(proyecto_id=id)
        kldc.KLDC = v_KLDC
        kldc.proyecto = proyecto
        kldc.save()

    diccionario_kldc = {'proyecto': proyecto,
                         'PFA': PFA,
                         'KLDC': v_KLDC,
                         'tabla_ldc': tabla_ldc,
                         'value': value,
                         'LDC': LDC,
                         }
    return diccionario_kldc
def Calcular_PF(id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    aspectos = get_object_or_404(AspectosANDComplejidad, pk=id)
    preguntas = preguntas_factores.objects.get(proyecto=proyecto)
    multiplicador = Multiplicador_Influencia.objects.get(proyecto=proyecto)

    operaciones = {'m1': aspectos.numEntradasBaja * 3,
                   'm2': aspectos.numEntradasMedia * 4,
                   'm3': aspectos.numEntradasAlta * 6,
                   'm4': aspectos.numSalidasBaja * 4,
                   'm5': aspectos.numSalidasMedia * 5,
                   'm6': aspectos.numSalidasAlta * 7,
                   'm7': aspectos.numConsultasBaja * 3,
                   'm8': aspectos.numConsultasMedia * 4,
                   'm9': aspectos.numConsultasAlta * 6,
                   'm10': aspectos.numArchivosInternosBaja * 7,
                   'm11': aspectos.numArchivosInternosMedia * 10,
                   'm12': aspectos.numArchivosInternosAlta * 15,
                   'm13': aspectos.numExternosBaja * 5,
                   'm14': aspectos.numExternosMedia * 7,
                   'm15': aspectos.numExternosAlta * 10,
                   }
    subtotal_baja = operaciones["m1"] + operaciones["m4"] + operaciones["m7"] + operaciones["m10"] + \
                    operaciones[
                        "m13"]
    subtotal_media = operaciones["m2"] + operaciones["m5"] + operaciones["m8"] + operaciones["m11"] + \
                     operaciones[
                         "m14"]
    subtotal_alta = operaciones["m3"] + operaciones["m6"] + operaciones["m9"] + operaciones["m12"] + \
                    operaciones[
                        "m15"]
    total = subtotal_baja + subtotal_media + subtotal_alta
    val_ajus_compl = multiplicador.Answer1 + multiplicador.Answer2 + multiplicador.Answer3 + multiplicador.Answer4 + multiplicador.Answer5 + multiplicador.Answer6
    val_ajus_compl += multiplicador.Answer7 + multiplicador.Answer8 + multiplicador.Answer9 + multiplicador.Answer10 + multiplicador.Answer11 + multiplicador.Answer12
    val_ajus_compl += multiplicador.Answer13 + multiplicador.Answer14

    fac_multi = 0.01 * val_ajus_compl
    sum = 0.65 + fac_multi
    PFA = total * sum
    if not PuntosFuncion.objects.filter(proyecto_id=id):
        PuntosFuncionAjustados = PuntosFuncion.objects.create(puntos_funcion_sin_ajustar=total,
                                                              puntos_funcion_ajustados=PFA,
                                                              multiplicador=val_ajus_compl, proyecto=proyecto)
        PuntosFuncionAjustados.save()
    else:
        pfa = PuntosFuncion.objects.get(proyecto_id=id)
        pfa.puntos_funcion_sin_ajustar = total
        pfa.puntos_funcion_ajustados = PFA
        pfa.multiplicador = val_ajus_compl
        pfa.proyecto = proyecto
        pfa.save()

    puntos_de_funcion = {'proyecto': proyecto,
                      'aspectos': aspectos,
                      'operaciones': operaciones,
                      'subtotal_baja': subtotal_baja,
                      'subtotal_media': subtotal_media,
                      'subtotal_alta': subtotal_alta,
                      'total': total,
                      'preguntas': preguntas,
                      'respuestas': multiplicador,
                      'val_ajus_compl': val_ajus_compl,
                      'fac_multi': fac_multi,
                      'PFA': PFA,
                      'sum': sum,
                      }
    return puntos_de_funcion

##modicar tabla
def editar_tabla_pf_ldc(request, id):
    if request.method == 'GET':
        print("dentro del get")
        proyecto = get_object_or_404(Proyecto, pk=id)
        usuario = proyecto.user
        tabla_ldc = LDCxPF.objects.get(user=usuario)
        atributos_valores = vars(tabla_ldc)
        atributos_valores = {key: value for key, value in atributos_valores.items() if
                             key not in ['id', '_state', 'user_id']}
        #Agregar tabla al diccionario
        return render(request, 'modal_tabla_pf_ldc.html', {'proyecto':proyecto,
                                                           'atributos_valores' : atributos_valores,
                                                           })

def CalcularPlaneacion(id):
    # CALCULAR LA PLANEACION 1ER ORDEN JONES
    proyecto = get_object_or_404(Proyecto, pk=id)
    PFA = PuntosFuncion.objects.get(proyecto=proyecto)
    tabla_planeacion = {'Pequeña escala' : 0.42,
                        'Mediana escala' : 0.43,
                        'Gran escala' : 0.45,
                        }
    tipo_proyecto = proyecto.tipo_proyecto
    exp = tabla_planeacion[tipo_proyecto]
    planeacion = round(pow(PFA.puntos_funcion_ajustados ,exp), 2)

    print(planeacion)
    # CALCULAR LA PLANEACION COCOMO
    kldc = KLDC.objects.get(proyecto=proyecto)
    ldcenmiles = kldc.KLDC
    tabla_cocomo = {'Pequeña escala' : (2.5,0.38),
                    'Mediana escala' : (2.5, 0.35),
                    'Gran escala' : (2.5, 0.32),
                    }
    tabla_esfuerzo = {'Pequeña escala' : (2.4,1.05),
                    'Mediana escala' : (3.0, 1.12),
                    'Gran escala' : (3.6, 1.20),
                    }
    coeficientes = tabla_esfuerzo[tipo_proyecto]
    ab, bb =coeficientes
    esfuerzo = round(ab * pow(ldcenmiles,bb),2)
    coeficientes = tabla_cocomo[tipo_proyecto]
    cb, db = coeficientes
    planeacion_cocomo = round(cb*pow(esfuerzo, db),2)

    diccionario_planeacion = {'planeacion' : planeacion,
                              'pfa' : PFA.puntos_funcion_ajustados,
                              'exp' : exp,
                              'ab' : ab,
                              'bb' : bb,
                              'esfuerzo' : esfuerzo,
                              'kldc' : ldcenmiles,
                              'planeacion_cocomo' : planeacion_cocomo,
                              'cb':cb,
                              'db' : db,
                              }


    return diccionario_planeacion

def Planeacion(request, id):
    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=id)
        planeacion = CalcularPlaneacion(id)
        return render(request, 'planeacion.html', {'proyecto':proyecto,
                                                   'planeacion' : planeacion,
                                                   })