from django.urls import path
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('',views.index,name ='index'),
    path('alunos/listar',views.listarAlunos,name='listar_alunos'),

    path('idiomas/listar',views.listarIdiomas,name='listar_alunos'),
]
