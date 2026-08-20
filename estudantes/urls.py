from django.urls import path

from estudantes import views

urlpatterns = [
    path('', views.listarEstudantes, name = 'listagem'),
    path('editar/', views.editarEstudantes, name = 'editar'),
    path('adicionar/', views.adicionarEstudante, name = 'adicionar'),
    path('listar/', views.listarEstudantes, name = 'listar'),
]
