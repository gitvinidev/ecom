from django import forms

from estudantes.models import Estudante


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        #fields = ('nome', 'email', 'telefone', 'nascimento', 'senha')
        fields= '__all__'



