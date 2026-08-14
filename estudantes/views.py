from django.shortcuts import render
from django.http import HttpResponse

# O arquivo views é onde definimos as nossas
# regras de negócios.

# Regra de negócio/método/função para listagem de estudantes.
def listarEstudantes(request):
    return HttpResponse('<h2>Olá estudantes, esta é a listagem<h2>')

def editarEstudantes(request):
    return HttpResponse('<h1>Editando estudante<h1>')