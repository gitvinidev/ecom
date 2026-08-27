from django.shortcuts import redirect, render
from django.http import HttpResponse

from estudantes.models import Estudante
from estudantes.forms import EstudanteForm

# O arquivo views é onde definimos as nossas
# regras de negócios.

# Regra de negócio/método/função para listagem de estudantes.
def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    contexto = {
        'listaEst' : estudantes,
    }
    return render(request, 'listagem.html', contexto)

def editarEstudantes(request, id=None):
    estudante = Estudante.objects.get(pk=id)
    form = EstudanteForm(request.POST or None, request.FILES or None, instance=estudante)
    if form.is_valid():
        form.save()
        return redirect('/')
    contexto = {
        'form' : form
    }
    return render(request, 'editar.html', contexto)
    

    return

def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    dicionario = {
        'form': form
    }
    return render(request, 'adicionar.html', dicionario)

def deletarEstudante(request, id=None):
    
    estudante = Estudante.objects.get(pk=id)
    #if request.method == 'POST':
    #    estudante.delete()
    #    return redirect('/')
    estudante.delete()
    return redirect('/')


