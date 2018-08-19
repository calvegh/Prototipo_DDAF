from django.urls import path
from django.conf.urls import url

from . import views, forms
from .views import MyCreateView

urlpatterns = [

    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('users/', views.users, name='users'),
    path('adduser/', views.adduser, name='adduser'),
    path('added/', views.added, name='added'),
    path('reclamos/', views.reclamos, name='reclamos'),
    path('indicadores/', views.indicadores, name='indicadores'),
    path('addcurso/', views.addcurso, name='addcurso'),
    path('addedcurso/', views.addedcurso, name='addedcurso'),
    url(r'^inscribircurso/(?P<pk>[0-9]+)/$',views.inscribircurso, name='inscribircurso'),
    url(r'^ver_alumnos_curso/(?P<pk>[0-9]+)/$',views.ver_alumnos_curso, name='ver_alumnos_curso'),
    url(r'^asistencias/(?P<pk>[0-9]+)/$', MyCreateView.as_view(), name='asistencias'),
    path('add_asistencia/', views.add_asistencia, name='add_asistencia'),

 ]

