from django.shortcuts import render
from sistema.models import Aluno

# view referente a listagem de alunos
def listarAlunos(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }

    return render(
        request,
        'alunos/listar.html',
        context,
    )