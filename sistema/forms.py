from django import forms
from .models import Aluno, Funcionario, Idioma


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','sobrenome','email','telefone','ativo','id_idioma',]

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','sobrenome','email','telefone','ativo','cargo',]

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['nome','unidade','professor','turno',]

