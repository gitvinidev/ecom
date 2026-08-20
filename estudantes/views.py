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

def editarEstudantes(request):
    return HttpResponse('<h1>Editando estudante<h1>')

def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    dicionario = {
        'form': form
    }
    return render(request, 'estudante.html', dicionario)

