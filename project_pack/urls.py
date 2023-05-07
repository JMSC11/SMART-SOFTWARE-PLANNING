#from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login,LoginView
from django.urls import path
from . import views
from .views import ReqFuncionalListView

#app_name = 'project_pack'
urlpatterns = [
    #path('', views.index, name='index'),
    path('gestion_proyectos/', views.gestion_proyectos, name='gestion_proyectos'),
    path('agregar_proyectos/', views.agregar_proyectos, name='agregar_proyectos'),
    path('Aspectos/', views.Aspectos, name='Aspectos'),
    path('agregar_multiplicador/', views.agregar_multiplicador, name='agregar_multiplicador'),
    path('macrofuncionalidad/', views.Macro, name='macrofuncionalidad'),
    path('req_funcional/', views.req_funcional, name = 'req_funcional'),
    path("ReqNoFuncionalListView/", views.ReqNoFuncionalListView, name="ReqNoFuncionalListView"),
    path("ReqFuncionalListView/", views.ReqFuncionalListView, name="ReqFuncionalListView"),
    path('req_no_funcional/', views.req_no_funcional, name = 'req_no_funcional'),
    path('detalles_proyecto/<id>', views.detalles_proyecto, name='detalles_proyecto'),
    path('eliminar_proyecto/<id>', views.eliminar_proyecto, name = 'eliminar_proyecto'),
    path('eliminar_macro/<id>', views.eliminar_macro, name='eliminar_macro'),
    path('eliminar_req_funcional/<id>', views.eliminar_req_funcional, name='eliminar_req_funcional'),
    path('eliminar_req_no_funcional/<id>', views.eliminar_req_no_funcional, name='eliminar_req_no_funcional'),
    path('editar_proyecto/<id>', views.editar_proyecto, name='editar_proyecto'),
    path('editar_funcional/<id>', views.editar_funcional, name='editar_funcional'),
    path('editar_no_funcional/<id>', views.editar_no_funcional, name='editar_no_funcional'),
    path('editar_aspectos/<id>', views.editar_aspectos, name='editar_aspectos'),
    path('editar_multiplicador/<id>', views.editar_multiplicador, name='editar_multiplicador'),
    path('editar_preguntas/<id>', views.editar_preguntas, name='editar_preguntas'),


]
