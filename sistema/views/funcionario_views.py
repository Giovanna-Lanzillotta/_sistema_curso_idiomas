from django.shortcuts import redirect, render
from sistema.forms import FuncionarioForm
from sistema.models import Funcionario

# view referente a listagem de funcionários
def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all()

    context = {
        'funcionarios': funcionarios,
    }

    return render(
        request,
        'funcionarios/listar.html',
        context,
    )


# Views referente a criação de funcionários
def CriarFuncionarios(request):

    if request.method == 'POST':
        form = FuncionarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios')
    else:
        form = FuncionarioForm()

    return render(
         request,
        'funcionarios/cadastro.html',
        {'form' : form},
        )