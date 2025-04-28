from django.shortcuts import redirect, render
from sistema.forms import IdiomaForm
from sistema.models import Idioma

# view referente a listagem de alunos
def listarIdiomas(request):
    idiomas = Idioma.objects.all()

    context = {
        'idiomas': idiomas,
    }

    return render(
        request,
        'idiomas/listar.html',
        context,
    )

# Views referente a criação de Idiomas
def CriarIdiomas(request):

    if request.method == 'POST':
        form = IdiomaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios')
    else:
        form = IdiomaForm()

    return render(
         request,
        'idiomas/cadastro.html',
        {'form' : form},
        )