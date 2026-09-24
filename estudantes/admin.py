from django.contrib import admin

from estudantes.models import Estudante

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'nascimento', 'senha')

# Register your models here.
admin.site.register(Estudante, EstudanteAdmin)
