from django.urls import path
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('',views.index,name ='index'),
    path('alunos',views.listarAlunos,name='listar_alunos'),
    path('alunos/novo',views.CriarAlunos,name='criar_alunos'),

    path('idiomas',views.listarIdiomas,name='listar_idiomas'),
    path('idiomas/novo',views.CriarIdiomas,name='criar_idiomas'),

    path('funcionarios',views.listarFuncionarios,name='listar_funcionarios'),
    path('funcionarios/novo',views.CriarFuncionarios,name='criar_funcionarios'),


]
