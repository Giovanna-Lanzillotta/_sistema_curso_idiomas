from django.shortcuts import render
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