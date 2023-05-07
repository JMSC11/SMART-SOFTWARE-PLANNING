from django.contrib.auth.decorators import login_required
import logging
from django.db import transaction
from django.shortcuts import render
from project_pack.proyecto import Proyecto
from project_pack.AspectosANDComplejidad import AspectosANDComplejidad
from project_pack.Multiplicador_Influencia import Multiplicador_Influencia
from project_pack.Requerimiento_Funcional import Requerimiento_Funcional
from project_pack.Requerimiento_no_Funcional import Requerimiento_no_Funcional
from project_pack.Macrofuncionalidad import Macrofuncionalidad
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
@login_required()
def Panel_Calculo(request):
    if request.method == 'GET':
        return render(request, 'Panel_Calculo.html')


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
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        lista_macrofuncionalidad = Macrofuncionalidad.objects.filter(proyecto=proyecto)
        lista_requerimientos = []
        for macro in lista_macrofuncionalidad:
            lista_requerimientos.extend(Requerimiento_Funcional.objects.filter(macrofuncionalidad=macro))
        print(lista_requerimientos)
        lista_no_funcionales = Requerimiento_no_Funcional.objects.filter(proyecto=proyecto)
        print(lista_no_funcionales)
        aspectos = AspectosANDComplejidad.objects.filter(proyecto=proyecto)
        print(aspectos)
        return render(request, 'Panel_Calculo.html', {'proyecto': proyecto,
                                                          'lista_macrofuncionalidad': lista_macrofuncionalidad,
                                                          'lista_requerimientos_funcionales' : lista_requerimientos,
                                                          'lista_no_funcionales': lista_no_funcionales,
                                                          'aspectos' : aspectos,
                                                          })
