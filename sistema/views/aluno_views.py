from django.shortcuts import redirect, render
from sistema.forms import AlunoForm
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


# Views referente a criação de alunos
def CriarAlunos(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/alunos')
    else:
        form = AlunoForm()

    return render(
         request,
        'alunos/cadastro.html',
        {'form' : form},
        )