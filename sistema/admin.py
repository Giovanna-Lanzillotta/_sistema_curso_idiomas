from django.contrib import admin

from sistema import models


#Funcionario
@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone','cargo','ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', )

#Idioma
@admin.register(models.Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','unidade','turno','professor',)
    search_fields = ('id', 'nome',)

#Aluno
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone','id_idioma', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome',)


