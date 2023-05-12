from django.contrib.auth.decorators import login_required
import logging
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .proyecto import Proyecto
from project_pack.AspectosANDComplejidad import AspectosANDComplejidad
from project_pack.Multiplicador_Influencia import Multiplicador_Influencia
from .Requerimiento_Funcional import Requerimiento_Funcional
from .Requerimiento_no_Funcional import Requerimiento_no_Funcional
from .Macrofuncionalidad import Macrofuncionalidad
from .preguntas_factores import preguntas_factores
from django.shortcuts import render, redirect, HttpResponse
# Vistas basadas en clases
from django.views.generic.list import ListView

@login_required()
def gestion_proyectos(request):
    if request.method == 'GET':
        user_id = request.user.id
        proyectos = Proyecto.objects.filter(user = user_id)
        #proyectos = Proyecto.objects.all()
        return render(request, 'gestion_proyectos.html', {'proyectos': proyectos})
        #return render(request, 'gestion_proyectos.html')
    else:
        print(request.POST)
        id_proyecto = request.POST['id_proyecto']
        name = request.POST['name']
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidad:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))

        lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)

        aspectos = AspectosANDComplejidad.objects.filter(proyecto=proyecto)

        preguntas = preguntas_factores.objects.filter(proyecto=proyecto)
        respuestas = Multiplicador_Influencia.objects.filter(proyecto=proyecto)
        print(preguntas)

        return render(request, 'detalles_proyecto.html', {'proyecto': proyecto,
                                                          'lista_macrofuncionalidad': lista_macrofuncionalidad,
                                                          'lista_requerimientos_funcionales' : lista_requerimientos,
                                                          'lista_no_funcionales': lista_no_funcionales,
                                                          'aspectos' : aspectos,
                                                          'preguntas' : preguntas,
                                                          'respuestas' : respuestas,
                                                          })

@login_required()
def agregar_proyectos(request):
    if request.method == 'GET':
        return render(request, 'agregar_proyectos.html')
    else: # Method == POST
        print(request.POST)

        try:
            usuario = request.user
            print(usuario)
            proyecto = Proyecto.objects.create(user=usuario, nombre=request.POST['nombre'], tipo_proyecto=request.POST['categoria'],
                                           lenguaje=request.POST('opcion'))
            proyecto.save()

            id_proyecto = proyecto.pk
            request.session['id_proyecto'] = id_proyecto
            #Agregar plantilla base de preguntas para el multiplicador de influencia.
            p1 = "¿Se requiere que el sistema sea responsivo?"
            p2 = "¿Se requiere comunicación de datos?"
            p3 = "¿Existen funciones de procesamiento distribuido?"
            p4 = "¿Es crítico el rendimiento?"
            p5 = "¿El sistema requiere una alta modularización?"
            p6 = "¿Requiere el sistema entrada de datos interactiva?"
            p7 = "¿Requiere la entrada de datos interactiva que las transacciones de entrada se lleven a cabo sobre múltiples pantallas u operaciones?"
            p8 = "¿El sistema considera una alta usabilidad, es decir?, ¿Se necesita que sea un sistema amigable para el usuario?"
            p9 = "¿Son complejas las entradas, las salidas, los archivos o las peticiones?"
            p10 = "¿Es complejo el procesamiento interno?"
            p11 = "¿Se ha diseñado el código para ser reutilizable?"
            p12 = "¿El sistema debe trabajar con otros sistemas? (Interoperabilidad)"
            p13 = "¿Se ha diseñado el sistema para soportar múltiples instalaciones en diferentes organizaciones?"
            p14 = "¿Se considera la seguridad de los datos y del sistema?"

            preguntas_base = preguntas_factores.objects.create(proyecto_id= id_proyecto, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14)
            preguntas_base.save()
            return redirect('macrofuncionalidad')
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar proyecto 3')


@login_required()
def Macro(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        return render(request, 'macrofuncionalidades.html', {
            'macrofuncionalidades': lista_macrofuncionalidad,
        })
        #requerimientos = Requerimiento_Funcional.objects.all()
    else: # Method == POST
        print(request.POST)
        try:
            id_proyecto = request.session.get('id_proyecto', None)
            print(id_proyecto)
            macrofuncionalidad = Macrofuncionalidad.objects.create(macrofuncionalidad=request.POST['macrofuncionalidad'], usuarios=request.POST['usuarios'], proyecto_id = id_proyecto)
            macrofuncionalidad.save()
            print(macrofuncionalidad)
            print("El id es: ")
            proyecto = Proyecto.objects.get(pk = id_proyecto)
            lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
            return render(request, 'macrofuncionalidades.html', {
                'message': 'Macrofuncionalidad agregada correctamente',
                'macrofuncionalidades': lista_macrofuncionalidad ,
                'x': 1
            })
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar macrofuncionalidad')

@login_required()
def req_funcional(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidades = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidades:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))
        return render(request, 'req_funcionales.html', {
            'lista_macrofuncionalidades' : lista_macrofuncionalidades,
            'lista_requerimientos': lista_requerimientos,
        })
    else: # Method == POST
        try:
            artefacto = request.POST['artefacto']
            if artefacto == 'funcional':
                id_funcional = request.session.get('id_funcional', None)
                funcional = get_object_or_404(Requerimiento_Funcional, pk=id_funcional)
                funcional.requerimiento = request.POST['requerimiento']
                funcional.descripcion = request.POST['descripcion']
                funcional.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                id_proyecto = request.session.get('id_proyecto', None)

                proyecto = Proyecto.objects.get(pk=id_proyecto)
                lista_macrofuncionalidades = Macrofuncionalidad.objects.filter(proyecto=proyecto)
                requerimiento = Requerimiento_Funcional.objects.create(requerimiento=request.POST['requerimiento'], descripcion=request.POST['descripcion'], macrofuncionalidad_id = request.POST['opcion'])
                requerimiento.save()
                print(requerimiento)
                lista_requerimientos  = []
                for macro in lista_macrofuncionalidades:
                    lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))

                return render(request, 'req_funcionales.html', {
                    'message': 'Requerimiento agregado correctamente',
                    'lista_macrofuncionalidades': lista_macrofuncionalidades,
                    'lista_requerimientos': lista_requerimientos,
                    'x': 1
                })
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar proyecto 3')

@login_required()
def req_no_funcional(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_requerimientos = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
        return render(request, 'req_no_funcionales.html', {
            'requerimientos': lista_requerimientos,
        })

    else: # Method == POST
        try:
            artefacto =  request.POST['artefacto']
            if artefacto == 'no_funcional':
                id_no_funcional = request.session.get('id_no_funcional', None)
                no_funcional = get_object_or_404(Requerimiento_no_Funcional, pk=id_no_funcional)
                no_funcional.requerimiento = request.POST['requerimiento']
                no_funcional.descripcion = request.POST['descripcion']
                no_funcional.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                id_proyecto = request.session.get('id_proyecto', None)
                lista_requerimientos_no_funcionales = request.POST.getlist('requerimiento')


                if len(lista_requerimientos_no_funcionales) != 0:
                    for req in lista_requerimientos_no_funcionales:
                        descrip = ''
                        if req == 'Confiabilidad':
                            descrip = 'Debe existir una baja probabilidad de que el sistema presente fallas'
                        elif req == 'Robustez':
                            descrip= 'El sistema debe responder adecuadamente cuando se presenten situaciones fuera de lo común'
                        elif req == 'Seguridad':
                            descrip= 'Que la información en el sistema esté protegida contra atacantes que pudieran causar daño.'
                        elif req == 'Portabilidad':
                            descrip= 'Que el sistema se pueda instalar con relativa facilidad en diferentes ambientes de hardware.'
                        elif req == 'Eficiencia o Rendimiento':
                            descrip= 'Que se consiga hacer la mayor cantidad de trabajo (calcular resultados, enviar mensajes, desplegar interfaces de usuario, etc.) con un uso mínimo de recursos (memoria, tiempo de procesamiento, ancho de banda, etc.)'
                        elif req == 'Reusabilidad':
                            descrip = 'Que el sistema o algunas de sus partes se puedan utilizar en la construcción de otros sistemas.'
                        elif req == 'Flexibilidad':
                            descrip = 'Que el sistema se pueda adaptar a otras circunstancias agregando o modificando módulos.'
                        elif req == 'Escalabilidad':
                            descrip= 'Se refiere a la capacidad del sistema de software de aumentar su rendimiento en la medida en que nuevos recursos de hardware son incorporados. '
                        elif req == 'Facilidad de pruebas':
                            descrip = 'Se refiere al nivel de complejidad de las pruebas efectuadas para asegurar la calidad del sistema de software.  '


                        requerimiento = Requerimiento_no_Funcional.objects.create(requerimiento=req, descripcion=descrip, proyecto_id = id_proyecto)
                        requerimiento.save()
                else:
                    requerimiento = Requerimiento_no_Funcional.objects.create(requerimiento=request.POST['requerimiento_p'] , descripcion=request.POST['descripcion'] , proyecto_id=id_proyecto)
                    requerimiento.save()
                    print(requerimiento)
                proyecto = Proyecto.objects.get(pk = id_proyecto)
                lista_requerimientos = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
                return render(request, 'req_no_funcionales.html', {
                    'message': 'Requerimiento agregado correctamente',
                    'x': 1,
                    'requerimientos': lista_requerimientos,
                })
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar proyecto 3')

@login_required()
def Aspectos(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidad:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))
        return render(request, 'Aspectos.html', {
            'lista_macrofuncionalidad': lista_macrofuncionalidad,
            'lista_requerimientos_funcionales': lista_requerimientos,
        })
    else: # Method == POST
        print(request.POST)

        try:
            id_proyecto = request.session.get('id_proyecto', None)
            aspectos = AspectosANDComplejidad.objects.create(numEntradasBaja = request.POST['num_In_Baja'] , numEntradasMedia = request.POST['num_In_Media'], numEntradasAlta = request.POST['num_In_Alta'] ,
                                                             numSalidasBaja = request.POST['num_Out_Baja'], numSalidasMedia =request.POST['num_Out_Media'], numSalidasAlta = request.POST['num_Out_Alta'],
                                                             numConsultasBaja= request.POST['num_Cons_baja'], numConsultasMedia = request.POST['num_Cons_Media'], numConsultasAlta =request.POST['num_Cons_Alta'],
                                                             numArchivosInternosBaja = request.POST['num_Inter_Baja'], numArchivosInternosMedia= request.POST['num_Inter_Media'], numArchivosInternosAlta = request.POST['num_Inter_Alta'],
                                                             numExternosBaja = request.POST['num_Ext_Baja'], numExternosMedia = request.POST['num_Ext_Media'], numExternosAlta =request.POST['num_Ext_Alta'], proyecto_id = id_proyecto)
            aspectos.save()
            print(aspectos)
            return redirect('agregar_multiplicador')
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar proyecto 3')
@login_required()
def agregar_multiplicador(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        preguntas_base = preguntas_factores.objects.get(proyecto_id=id_proyecto)
        print(preguntas_base)
        return render(request, 'multiplicador_Influencia.html', {
            'preguntas_base': preguntas_base,
            'proyecto' : proyecto,
        })
    else: # Method == POST
        print(request.POST)
        artefacto = request.POST['artefacto']
        id_proyecto = request.session.get('id_proyecto', None)
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        if artefacto == 'preguntas':
            preguntas_base = preguntas_factores.objects.get(proyecto_id = id_proyecto)
            preguntas_base.p1 = request.POST['P1']
            preguntas_base.p2 = request.POST['P2']
            preguntas_base.p3 = request.POST['P3']
            preguntas_base.p4 = request.POST['P4']
            preguntas_base.p5 = request.POST['P5']
            preguntas_base.p6 = request.POST['P6']
            preguntas_base.p7 = request.POST['P7']
            preguntas_base.p8 = request.POST['P8']
            preguntas_base.p9 = request.POST['P9']
            preguntas_base.p10 = request.POST['P10']
            preguntas_base.p11 = request.POST['P11']
            preguntas_base.p12 = request.POST['P12']
            preguntas_base.p13 = request.POST['P13']
            preguntas_base.p14 = request.POST['P14']
            preguntas_base.save()
            return render(request, 'multiplicador_Influencia.html', {
                'preguntas_base': preguntas_base,
                'proyecto' : proyecto,
        })
        try:
            id_proyecto = request.session.get('id_proyecto', None)
            multi = Multiplicador_Influencia.objects.create(Answer1 = request.POST['A1'], Answer2 = request.POST['A2'], Answer3 = request.POST['A3'],
                                                            Answer4 = request.POST['A4'], Answer5 = request.POST['A5'], Answer6 = request.POST['A6'],
                                                            Answer7 = request.POST['A7'], Answer8 = request.POST['A8'], Answer9 = request.POST['A9'],
                                                            Answer10 = request.POST['A10'], Answer11= request.POST['A11'], Answer12 = request.POST['A12'],
                                                            Answer13 = request.POST['A13'], Answer14 = request.POST['A14'], proyecto_id = id_proyecto)
            multi.save()
            print(multi)
            return redirect('gestion_proyectos')
        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al agregar proyecto 3')

@login_required()
def detalles_proyecto(request, id):
    if request.method == 'GET':
        id_proyecto = id
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        request.session['id_proyecto'] = id_proyecto

        name = proyecto.nombre

        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidad:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))

        lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)

        aspectos = AspectosANDComplejidad.objects.filter(proyecto=proyecto)

        preguntas = preguntas_factores.objects.get(proyecto=proyecto)
        multiplicador = Multiplicador_Influencia.objects.get(proyecto=proyecto)

        return render(request, 'detalles_proyecto.html', {'proyecto': proyecto,
                                                          'lista_macrofuncionalidad': lista_macrofuncionalidad,
                                                          'lista_requerimientos_funcionales': lista_requerimientos,
                                                          'lista_no_funcionales': lista_no_funcionales,
                                                          'aspectos': aspectos,
                                                          'preguntas' : preguntas,
                                                          'respuestas' : multiplicador,
                                                          })

    else:
        proyecto = get_object_or_404(Proyecto, pk=id)

        try:
            artefacto = request.POST['artefacto']

            if artefacto == 'proyecto':
                usuario = request.user
                print(usuario)
                proyecto.user = usuario
                proyecto.nombre = request.POST['nombre']
                proyecto.tipo_proyecto = request.POST['categoria']
                proyecto.lenguaje = request.POST.('opcion')

                proyecto.save()
                return redirect('detalles_proyecto', id)
            elif artefacto == 'funcional':
                id_funcional = request.session.get('id_funcional', None)
                funcional = get_object_or_404(Requerimiento_Funcional, pk=id_funcional)
                funcional.requerimiento = request.POST['requerimiento']
                funcional.descripcion = request.POST['descripcion']
                funcional.save()
                return redirect('detalles_proyecto', id)
            elif artefacto == 'no_funcional':
                id_no_funcional = request.session.get('id_no_funcional', None)
                no_funcional = get_object_or_404(Requerimiento_no_Funcional, pk=id_no_funcional)
                no_funcional.requerimiento = request.POST['requerimiento']
                no_funcional.descripcion = request.POST['descripcion']
                no_funcional.save()
                return redirect('detalles_proyecto', id)
            elif artefacto == 'aspectos':
                aspectos = AspectosANDComplejidad.objects.get(proyecto_id=id)

                aspectos.numEntradasBaja = request.POST['num_In_Baja']
                aspectos.numEntradasMedia = request.POST['num_In_Media']
                aspectos.numEntradasAlta = request.POST['num_In_Alta']
                aspectos.numSalidasBaja = request.POST['num_Out_Baja']
                aspectos.numSalidasMedia = request.POST['num_Out_Media']
                aspectos.numSalidasAlta = request.POST['num_Out_Alta']
                aspectos.numConsultasBaja = request.POST['num_Cons_Baja']
                aspectos.numConsultasMedia = request.POST['num_Cons_Media']
                aspectos.numConsultasAlta = request.POST['num_Cons_Alta']
                aspectos.numArchivosInternosBaja = request.POST['num_Inter_Baja']
                aspectos.numArchivosInternosMedia = request.POST['num_Inter_Media']
                aspectos.numArchivosInternosAlta = request.POST['num_Inter_Alta']
                aspectos.numExternosBaja = request.POST['num_Ext_Baja']
                aspectos.numExternosMedia = request.POST['num_Ext_Media']
                aspectos.numExternosAlta = request.POST['num_Ext_Alta']
                aspectos.save()
                return redirect('detalles_proyecto', id)
            elif artefacto == 'multiplicador':
                preguntas = preguntas_factores.objects.get(proyecto_id = id)
                respuestas = Multiplicador_Influencia.objects.get(proyecto_id = id)

                preguntas.p1 = request.POST['P1']
                preguntas.p2 = request.POST['P2']
                preguntas.p3 = request.POST['P3']
                preguntas.p4 = request.POST['P4']
                preguntas.p5 = request.POST['P5']
                preguntas.p6 = request.POST['P6']
                preguntas.p7 = request.POST['P7']
                preguntas.p8 = request.POST['P8']
                preguntas.p9 = request.POST['P9']
                preguntas.p10 = request.POST['P10']
                preguntas.p11 = request.POST['P11']
                preguntas.p12 = request.POST['P12']
                preguntas.p13 = request.POST['P13']
                preguntas.p14 = request.POST['P14']


                respuestas.Answer1 = request.POST['A1']
                respuestas.Answer2 = request.POST['A2']
                respuestas.Answer3 = request.POST['A3']
                respuestas.Answer4 = request.POST['A4']
                respuestas.Answer5 = request.POST['A5']
                respuestas.Answer6 = request.POST['A6']
                respuestas.Answer7 = request.POST['A7']
                respuestas.Answer8 = request.POST['A8']
                respuestas.Answer9 = request.POST['A9']
                respuestas.Answer10 = request.POST['A10']
                respuestas.Answer11 = request.POST['A11']
                respuestas.Answer12 = request.POST['A12']
                respuestas.Answer13 = request.POST['A13']
                respuestas.Answer14 = request.POST['A14']
                respuestas.save()
                preguntas.save()

                return redirect('detalles_proyecto', id)


        except Exception as e:
            logging.exception(e)
            return HttpResponse('Error al editar proyecto')


def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    if request.method == 'GET':
        print("dentro del get")
        return render(request, 'modal-edicion-proyecto.html', {
            'proyecto': proyecto,
        })


def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))



def eliminar_macro(request, id):
    macro = Macrofuncionalidad.objects.get(id=id)
    macro.delete()
    return redirect('macrofuncionalidad')

def eliminar_req_funcional(request, id):
    requerimiento = Requerimiento_Funcional.objects.get(id=id)
    requerimiento.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def editar_funcional(request, id):
    req_funcional = get_object_or_404(Requerimiento_Funcional, pk=id)
    request.session['id_funcional'] = id
    id_proyecto = request.session.get('id_proyecto', None)
    proyecto = get_object_or_404(Proyecto, pk=id_proyecto)

    if request.method == 'GET':
        return render(request, 'modal-edicion-req-funcional.html', {
            'req_funcional': req_funcional,
            'proyecto' : proyecto,
            'templete' : 'req_funcional',
        })

def editar_no_funcional(request, id):
    req_no_funcional = get_object_or_404(Requerimiento_no_Funcional, pk=id)
    request.session['id_no_funcional'] = id
    id_proyecto = request.session.get('id_proyecto', None)
    proyecto = get_object_or_404(Proyecto, pk=id_proyecto)

    if request.method == 'GET':
        return render(request, 'modal-edicion-req-no-funcional.html', {
            'req_no_funcional': req_no_funcional,
            'proyecto' : proyecto,
        })

def editar_aspectos(request, id):
    print(id)
    #proyecto_id = id
    #aspectos = get_object_or_404(AspectosANDComplejidad, pk=proyecto_id)
    proyecto = get_object_or_404(Proyecto, pk=id)
    aspectos = AspectosANDComplejidad.objects.get(proyecto_id=proyecto)
    if request.method == 'GET':
        return render(request, 'modal_aspectos.html', {
            'aspectos': aspectos,
            'proyecto': proyecto,
        })

def editar_multiplicador(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    preguntas = preguntas_factores.objects.get(proyecto_id=id)
    respuestas = Multiplicador_Influencia.objects.get(proyecto_id=id)
    lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
    if request.method == 'GET':
        return render(request, 'modal_multiplicador.html', {
            'preguntas': preguntas,
            'respuestas': respuestas,
            'proyecto': proyecto,
            'lista_no_funcionales': lista_no_funcionales,
        })

def editar_preguntas(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    preguntas = preguntas_factores.objects.get(proyecto_id=id)
    lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
    if request.method == 'GET':
        return render(request, 'modal_preguntas.html', {
            'preguntas': preguntas,
            'proyecto': proyecto,
            'lista_no_funcionales': lista_no_funcionales,
        })
def eliminar_req_no_funcional(request, id):
    requerimiento = Requerimiento_no_Funcional.objects.get(id=id)
    requerimiento.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
@login_required()
def ReqFuncionalListView(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidad:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))
        return render(request, 'requerimiento_funcional_list.html', {
            'lista_macrofuncionalidad': lista_macrofuncionalidad,
            'lista_requerimientos_funcionales': lista_requerimientos,
            'proyecto': proyecto,
        })


@login_required()
def ReqNoFuncionalListView(request):
    if request.method == 'GET':
        id_proyecto = request.session.get('id_proyecto', None)
        request.session['id_proyecto'] = id_proyecto
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_requerimientos_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)

        return render(request, 'req_no_funcional_list.html', {
            'lista_requerimientos_no_funcionales': lista_requerimientos_no_funcionales,
            'proyecto': proyecto,
        })
